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

Also, usually flux2 resources are used for e.g. Helm, so flux2 controllers need to be installed in any destination cluster.

## Automated smoke tests

In order to ensure that every component inside of SCS behaves as
expected, there should be simple smoke tests.
These tests are implemented using GitHub Actions/Workflows.

## References

| | |
| --- | --- |
| CI smoke test | ![Smoke test](https://github.com/SovereignCloudStack/k8s-{{ name_path }}/workflows/CI/badge.svg) |
{% for reference in references -%}
| {{ reference.type }} | {% if reference.isBadge %}!{% endif %}[{{ reference.name }}]({{reference.href}}) |
{% endfor %}

{% if appendix %}
## Further information

{{ appendix }}

{% endif %}
