scores={'张三':100,'李四':98,'王五':45}
for a in scores:
    print(a,scores[a])
    print(a, scores.get(a))