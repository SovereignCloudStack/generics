# generics
  
Central place for CI scripts and unified templates like README
files.

## Workflow

1. Changes in this repository must first be added to the corresponding template
   for new projects and successfully verified by the CI.

   The change made in the template must be referenced in the commit message.

2. The change is processed (use of templates, ..) and added to the corresponding
   directories (``k8s``, ``github``).

3. The changes can then be applied to all repositories using
   [Gilt](https://github.com/metacloud/gilt).

## Templates for new projects

* K8S: https://github.com/SovereignCloudStack/k8s-template
