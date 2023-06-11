const { awscdk } = require('projen');
const { Stability } = require('projen/lib/cdk');
const { UpgradeDependenciesSchedule } = require('projen/lib/javascript');

const project = new awscdk.AwsCdkConstructLibrary({
  authorName: 'Stefan Freitag',
  authorEmail: 'stefan.freitag@rwe.com',
  authorOrganization: false,
  cdkVersion: '2.83.0',
  //majorVersion: 1,
  defaultReleaseBranch: 'main',
  description: 'Notifies on new AWS ECR scan results',
  depsUpgradeOptions: {
    workflowOptions: {
      schedule: UpgradeDependenciesSchedule.MONTHLY,
    },
  },
  repository: 'https://github.com/stefanfreitag/cdk-ecr-scan-notifier.git',
  stability: Stability.STABLE,
  keywords: ['aws', 'cdk', 'ecr', 'sns'],
  name: 'ecr-scan-notifier',
  publishToPypi: {
    module: 'ecr_scan_notifier',
    distName: 'ecr-scan-notifier',
  },
  publishToMaven: {
    javaPackage: 'io.github.stefanfreitag',
    mavenGroupId: 'io.github.stefanfreitag',
    mavenArtifactId: 'ecrScanNotifier',
  },

  publishToNuget: {
    dotNetNamespace: 'Io.Github.StefanFreitag',
    packageId: 'Io.Github.StefanFreitag.ecrscannotifier',
  },

});

const common_exclude = ['.history/', '.venv', '.idea', '__pycache__', '.coverage'];

project.gitignore.exclude(...common_exclude);
project.npmignore.exclude(...common_exclude);


project.synth();