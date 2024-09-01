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



