

### Development

```
docker build --progress=plain --no-cache -t uptimekuma_homer:latest .
```

```
docker run --rm -it \
    -e UKH_PORT=${UKH_PORT} \
    -t uptimekuma_homer:latest
```
