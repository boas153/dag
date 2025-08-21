dags:
  persistence:
    enabled: true
    existingClaim: ""
    size: 1Gi
    accessMode: ReadWriteMany
  hostPath:
    enabled: true
    path: /Users/youngho/dev/airflow-dags

