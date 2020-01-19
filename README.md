A simple Blockchain in Python that I built following Daniel van Flymen's (https://github.com/dvf) excellent medium [article](https://medium.com/@vanflymen/learn-blockchains-by-building-one-117428612f46).

### Some basic command-line examples

- Start node with default port

```
./venv/bin/python3.8 blockchain-added-port-params.py
```

- Start node with port 5000

```
./venv/bin/python3.8 blockchain-added-port-params.py -p 5000
```

- Start node with port 5001

```
./venv/bin/python3.8 blockchain-added-port-params.py -p 5001
```

### API access examples via [HTTPie](https://github.com/jakubroztocil/httpie)

- Mine block using :5000 node

```
http GET http://0.0.0.0:5000/mine
```

- Post new transaction to :5000 node

```
http POST http://0.0.0.0:5000/transactions/new \
    sender=1uWiCHVaTb2GXJn6jUpNUnwzrZoPFyW2d \
    recipient=1Aaqx87nkHg42WsTMR5kNXPBnNrHp1sGXr \
    amount:=50
```

- Get entire Blockchain from :5000 node

```
http GET http://0.0.0.0:5000/chain
```

- Register another node with :5000 node

```
echo '{
    "nodes": ["http://localhost:5001"]
}' | http --json POST http://localhost:5000/nodes/register
```

- Resolve chain conflicts and switch to largest valid chain

```
http GET http://0.0.0.0:5000/nodes/resolve
```
