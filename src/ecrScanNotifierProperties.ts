import { RetentionDays } from 'aws-cdk-lib/aws-logs';

export interface EcrScanNotifierProperties {
  /**
   * ARN of the topic to forwardd the ECR scan results to.
   *
   * @type {string}
   * @memberof EcrScanNotifierProperties
   */
  readonly topicArn: string;

  /**
   * ARN of the topics encryption key.
   *
   * @type {string}
   * @memberof EcrScanNotifierProperties
   */
  readonly keyArn?: string;
  /**
   * Number of days to keep the log files.
   *
   * @type {RetentionDays}
   * @default RetentionDays.ONE_MONTH
   * @memberof EcrScanNotifierProperties
   */
  readonly logRetentionDays?: RetentionDays;
}
