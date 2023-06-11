import { App, Stack } from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import { EcrScanNotifier } from '../src/';

test('Default values for Lambda function', () => {
  const app = new App();
  const stack = new Stack(app, 'test');
  new EcrScanNotifier(stack, 'test', {
    topicArn: 'arn_of_topic',
    logRetentionDays: RetentionDays.ONE_WEEK,
  });

  const template = Template.fromStack(stack);
  template.hasResourceProperties('AWS::Lambda::Function', {
    Description: 'Send ECR Image Scan findings to Microsoft Teams channel',
    Handler: 'index.handler',
    MemorySize: 128,
    Runtime: 'python3.9',
    Timeout: 60,
    Environment: {
      Variables: {
        TOPIC_ARN: 'arn_of_topic',
      },
    },
  });
});

test('Default values for Eventbus Rule', () => {
  const app = new App();
  const stack = new Stack(app, 'test');
  new EcrScanNotifier(stack, 'test', {
    topicArn: 'arn_of_topic',
  });

  const template = Template.fromStack(stack);
  template.hasResourceProperties('AWS::Events::Rule', {
    Description: 'Send ECR Image Scan findings to Microsoft Teams channel',
    EventPattern: {
      'source': [
        'aws.ecr',
        'aws.inspector2',
      ],
      'detail-type': [
        'ECR Image Scan',
        'Inspector2 Scan',
      ],
    },
  });
});
