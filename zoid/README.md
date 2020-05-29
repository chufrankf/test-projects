Start child
```
cd child
python3 -m http.server 9001

# to start with x-frame-options=sameorigin server use
python3 ../xframeserver.py 9001
```

Start parent
```
cd zoid-parent
python3 -m http.server 9002
```