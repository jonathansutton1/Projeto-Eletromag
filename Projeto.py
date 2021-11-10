def CalcularTransformador(Uf, Rc):
    Z=np.array([[R1+XL1, -XM],[-XM, XL2+R2+Rc]])
    V=np.array([Uf,0])
    i=np.dot(linalg.inv(Z),V)
    return i[0], i[1]