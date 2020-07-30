# Deployment manifests for {{ name_title|join('/') }}
{% if attributions %}
## Attributions
{% for attribution in attributions %}
{{attribution.trademark}} is a trademark of {{attribution.owner}} which is not affiliated with the SCS project.
{% endfor %}{% endif %}
## Repository content

This repository is intended to include all relevant configuration
and Kubernetes manifests for the deployment of {{ name_description }} inside SCS.

## Repository layout

This repository contains kustomize bases which may be referenced by
kustomize overlays which in turn define the deployment of whole
environments/clusters.

## Automated smoke tests

In order to ensure that every component inside of SCS behaves as
expected, there should be simple smoke tests.
These tests are implemented using GitHub Actions/Workflows.

{% if appendix %}
## Further information

{{ appendix }}

{% endif %}
