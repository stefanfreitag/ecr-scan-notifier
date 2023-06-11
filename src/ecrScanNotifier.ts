import { execSync } from 'child_process';
import * as path from 'path';

import { Duration } from 'aws-cdk-lib';
import { Rule } from 'aws-cdk-lib/aws-events';
import { LambdaFunction } from 'aws-cdk-lib/aws-events-targets';
import { Effect, Policy, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import { EcrScanNotifierProperties } from './ecrScanNotifierProperties';

export class EcrScanNotifier extends Construct {
  props: EcrScanNotifierProperties;

  constructor(scope: Construct, id: string, props: EcrScanNotifierProperties) {
    super(scope, id);

    this.props = props;
    const handler = this.createFunction();

    const ecrScanTarget = new LambdaFunction(handler);
    new Rule(this, 'EventBusEcrImageScan', {
      ruleName: 'EventBusEcrImageScanRule',
      description: 'Send ECR Image Scan findings to Microsoft Teams channel',
      targets: [ecrScanTarget],
      eventPattern: {
        source: ['aws.ecr', 'aws.inspector2'],
        detailType: ['ECR Image Scan', 'Inspector2 Scan'],
      },
    });
  }
  private createFunction(): Function {
    const function_dir = path.join(__dirname, '../lambda/');

    const fn = new Function(this, 'ecr-scan-notifier', {
      runtime: Runtime.PYTHON_3_9,
      handler: 'index.handler',
      code: Code.fromAsset(function_dir, {
        bundling: {
          image: Runtime.PYTHON_3_9.bundlingImage,
          local: {
            tryBundle(outputDir: string) {
              try {
                execSync('pip3 --version');
              } catch {
                return false;
              }

              execSync(
                `pip install -r ${path.join(
                  function_dir,
                  'requirements.txt',
                )} -t ${path.join(outputDir)}`,
              );
              execSync(`cp -au ${function_dir}/* ${path.join(outputDir)}`);
              return true;
            },
          },
        },
      }),
      environment: {
        TOPIC_ARN: this.props.topicArn,
      },
      timeout: Duration.minutes(1),
      memorySize: 128,
      logRetention: this.props.logRetentionDays
        ? this.props.logRetentionDays
        : RetentionDays.ONE_MONTH,
      description: 'Send ECR Image Scan findings to Microsoft Teams channel',
    });

    let statements: PolicyStatement[] = [];
    statements.push(
      new PolicyStatement({
        effect: Effect.ALLOW,
        actions: ['sns:Publish'],
        resources: [this.props.topicArn],
      }),
    );
    if (this.props.keyArn) {
      statements.push(
        new PolicyStatement({
          effect: Effect.ALLOW,
          actions: ['kms:Decrypt', 'kms:GenerateDataKey'],
          resources: [this.props.keyArn!],
        }),
      );
    }

    fn.role?.attachInlinePolicy(
      new Policy(this, 'sns-publish', {
        statements,
      }),
    );
    return fn;
  }
}
