# CDK ECR Scan Notifier

A CDK construct capable of forwarding ECR scan results to an SNS topic.

## Sample Events

- ECR Basic Scan

   ```json
   {
      "version":"0",
      "id":"822c3bbb-574a-8d0b-828e-b33e93cc0b3a",
      "detail-type":"ECR Image Scan",
      "source":"aws.ecr",
      "account":"012345678912",
      "time":"2022-08-03T18:14:18Z",
      "region":"eu-central-1",
      "resources":[
         "arn:aws:ecr:eu-central-1:012345678912:repository/sampleapp"
      ],
      "detail":{
         "scan-status":"COMPLETE",
         "repository-name":"sampleapp",
         "image-digest":"sha256:5b5a96370efd56ae20a832244ae56e8e57b1035f493f728eb6cef026586782f7",
         "image-tags":[
            "3862",
            "latest"
         ],
         "finding-severity-counts":{
            "HIGH":3,
            "MEDIUM":14,
            "INFORMATIONAL":3,
            "LOW":1,
            "HIGH":2
         }
      }
   }
   ```

- AWS Inspector

   ```json
   {
      "version":"0",
      "id":"961d7f4a-f46c-b376-f92f-f8c3af290f9f",
      "detail-type":"Inspector2 Scan",
      "source":"aws.inspector2",
      "account":"520666953574",
      "time":"2022-09-14T19:12:46Z",
      "region":"eu-central-1",
      "resources":[
         "arn:aws:ecr:eu-central-1:520666953574:repository/azure-agent"
      ],
      "detail":{
         "scan-status":"INITIAL_SCAN_COMPLETE",
         "repository-name":"arn:aws:ecr:eu-central-1:520666953574:repository/azure-agent",
         "finding-severity-counts":{
            "CRITICAL":0,
            "HIGH":1,
            "MEDIUM":6,
            "TOTAL":10
         },
         "image-digest":"sha256:734a4d019b381f591a63c819ae88b00eed5dba8b76626530c26497128a6c46d1",
         "image-tags":[
            "latest",
            "5715"
         ]
      }
   }
   ```

## Links

- [Image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
# API Reference <a name="API Reference" id="api-reference"></a>

## Constructs <a name="Constructs" id="Constructs"></a>

### EcrScanNotifier <a name="EcrScanNotifier" id="ecr-scan-notifier.EcrScanNotifier"></a>

#### Initializers <a name="Initializers" id="ecr-scan-notifier.EcrScanNotifier.Initializer"></a>

```typescript
import { EcrScanNotifier } from 'ecr-scan-notifier'

new EcrScanNotifier(scope: Construct, id: string, props: EcrScanNotifierProperties)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#ecr-scan-notifier.EcrScanNotifier.Initializer.parameter.scope">scope</a></code> | <code>constructs.Construct</code> | *No description.* |
| <code><a href="#ecr-scan-notifier.EcrScanNotifier.Initializer.parameter.id">id</a></code> | <code>string</code> | *No description.* |
| <code><a href="#ecr-scan-notifier.EcrScanNotifier.Initializer.parameter.props">props</a></code> | <code><a href="#ecr-scan-notifier.EcrScanNotifierProperties">EcrScanNotifierProperties</a></code> | *No description.* |

---

##### `scope`<sup>Required</sup> <a name="scope" id="ecr-scan-notifier.EcrScanNotifier.Initializer.parameter.scope"></a>

- *Type:* constructs.Construct

---

##### `id`<sup>Required</sup> <a name="id" id="ecr-scan-notifier.EcrScanNotifier.Initializer.parameter.id"></a>

- *Type:* string

---

##### `props`<sup>Required</sup> <a name="props" id="ecr-scan-notifier.EcrScanNotifier.Initializer.parameter.props"></a>

- *Type:* <a href="#ecr-scan-notifier.EcrScanNotifierProperties">EcrScanNotifierProperties</a>

---

#### Methods <a name="Methods" id="Methods"></a>

| **Name** | **Description** |
| --- | --- |
| <code><a href="#ecr-scan-notifier.EcrScanNotifier.toString">toString</a></code> | Returns a string representation of this construct. |

---

##### `toString` <a name="toString" id="ecr-scan-notifier.EcrScanNotifier.toString"></a>

```typescript
public toString(): string
```

Returns a string representation of this construct.

#### Static Functions <a name="Static Functions" id="Static Functions"></a>

| **Name** | **Description** |
| --- | --- |
| <code><a href="#ecr-scan-notifier.EcrScanNotifier.isConstruct">isConstruct</a></code> | Checks if `x` is a construct. |

---

##### ~~`isConstruct`~~ <a name="isConstruct" id="ecr-scan-notifier.EcrScanNotifier.isConstruct"></a>

```typescript
import { EcrScanNotifier } from 'ecr-scan-notifier'

EcrScanNotifier.isConstruct(x: any)
```

Checks if `x` is a construct.

###### `x`<sup>Required</sup> <a name="x" id="ecr-scan-notifier.EcrScanNotifier.isConstruct.parameter.x"></a>

- *Type:* any

Any object.

---

#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#ecr-scan-notifier.EcrScanNotifier.property.node">node</a></code> | <code>constructs.Node</code> | The tree node. |
| <code><a href="#ecr-scan-notifier.EcrScanNotifier.property.props">props</a></code> | <code><a href="#ecr-scan-notifier.EcrScanNotifierProperties">EcrScanNotifierProperties</a></code> | *No description.* |

---

##### `node`<sup>Required</sup> <a name="node" id="ecr-scan-notifier.EcrScanNotifier.property.node"></a>

```typescript
public readonly node: Node;
```

- *Type:* constructs.Node

The tree node.

---

##### `props`<sup>Required</sup> <a name="props" id="ecr-scan-notifier.EcrScanNotifier.property.props"></a>

```typescript
public readonly props: EcrScanNotifierProperties;
```

- *Type:* <a href="#ecr-scan-notifier.EcrScanNotifierProperties">EcrScanNotifierProperties</a>

---


## Structs <a name="Structs" id="Structs"></a>

### EcrScanNotifierProperties <a name="EcrScanNotifierProperties" id="ecr-scan-notifier.EcrScanNotifierProperties"></a>

#### Initializer <a name="Initializer" id="ecr-scan-notifier.EcrScanNotifierProperties.Initializer"></a>

```typescript
import { EcrScanNotifierProperties } from 'ecr-scan-notifier'

const ecrScanNotifierProperties: EcrScanNotifierProperties = { ... }
```

#### Properties <a name="Properties" id="Properties"></a>

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| <code><a href="#ecr-scan-notifier.EcrScanNotifierProperties.property.topicArn">topicArn</a></code> | <code>string</code> | ARN of the topic to forwardd the ECR scan results to. |
| <code><a href="#ecr-scan-notifier.EcrScanNotifierProperties.property.keyArn">keyArn</a></code> | <code>string</code> | ARN of the topics encryption key. |
| <code><a href="#ecr-scan-notifier.EcrScanNotifierProperties.property.logRetentionDays">logRetentionDays</a></code> | <code>aws-cdk-lib.aws_logs.RetentionDays</code> | Number of days to keep the log files. |

---

##### `topicArn`<sup>Required</sup> <a name="topicArn" id="ecr-scan-notifier.EcrScanNotifierProperties.property.topicArn"></a>

```typescript
public readonly topicArn: string;
```

- *Type:* string

ARN of the topic to forwardd the ECR scan results to.

---

##### `keyArn`<sup>Optional</sup> <a name="keyArn" id="ecr-scan-notifier.EcrScanNotifierProperties.property.keyArn"></a>

```typescript
public readonly keyArn: string;
```

- *Type:* string

ARN of the topics encryption key.

---

##### `logRetentionDays`<sup>Optional</sup> <a name="logRetentionDays" id="ecr-scan-notifier.EcrScanNotifierProperties.property.logRetentionDays"></a>

```typescript
public readonly logRetentionDays: RetentionDays;
```

- *Type:* aws-cdk-lib.aws_logs.RetentionDays
- *Default:* RetentionDays.ONE_MONTH

Number of days to keep the log files.

---



