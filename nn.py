from sknn.mlp import Classifier, Layer

nn = Classifier(
    layers=[
        Layer("Rectifier", units=100),
        Layer("Softmax")],
    learning_rate=0.02,
    n_iter=10)
nn.fit(X_train, y_train)

y_valid = nn.predict(X_valid)

score = nn.score(X_test, y_test)
