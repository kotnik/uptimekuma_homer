

### Development

```
docker build --progress=plain --no-cache -t uptimekuma_homer:latest .
```

```
curl -u":${UKH_API_KEY}" $UKH_HOST/metrics
```

```
docker run --rm -it \
    -e UKH_PORT=${UKH_PORT} \
    -t uptimekuma_homer:latest
```
