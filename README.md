

### Development

```
docker build --progress=plain --no-cache -t uptimekuma_homer:latest .
```

```
curl -u":${UKH_API_KEY}" $UKH_HOST/metrics
```

```
docker run --rm -it               \
    -e UKH_PORT=${UKH_PORT}       \
    -e UKH_HOST=${UKH_HOST}       \
    -e UKH_API_KEY=${UKH_API_KEY} \
    -t uptimekuma_homer:latest
```

### Release

```
git tag -a -m '1.0' 1.0
docker build -t uptimekuma_homer:1.0 .

docker tag uptimekuma_homer:1.0 192.168.88.136:5000/uptimekuma_homer:1.0
docker tag uptimekuma_homer:1.0 192.168.88.136:5000/uptimekuma_homer:latest

docker push 192.168.88.136:5000/uptimekuma_homer:1.0
docker push 192.168.88.136:5000/uptimekuma_homer:latest
```

