from rediscluster import RedisCluster

if __name__ == '__main__':
    nodes = [{"host": "localhost", "port": "6379"}]
    r = RedisCluster(startup_nodes=nodes)
    r.set('test', "from this to this s")
    print(r.get('test'))
