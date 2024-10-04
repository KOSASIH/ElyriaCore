from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from domain.medical_record import MedicalRecord

class MedicalRecordModel:
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=(10,)))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, medical_records: [MedicalRecord]):
        X = [medical_record.to_dict() for medical_record in medical_records]
        y = [medical_record.has_complication for medical_record in medical_records]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
        y_pred = self.model.predict(X_test)
        y_pred_class = [1 if pred > 0.5 else 0 for pred in y_pred]
        print('Accuracy:', accuracy_score(y_test, y_pred_class))

    def predict(self, medical_record: MedicalRecord):
        medical_record_data = medical_record.to_dict()
        prediction = self.model.predict(medical_record_data)
        return prediction > 0.5

    def save(self, filename: str):
        self.model.save(filename)

    def load(self, filename: str):
        self.model.load_weights(filename)
