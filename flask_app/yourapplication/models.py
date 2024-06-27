from yourapplication.extensions import db, bcrypt
from yourapplication.extensions import db, bcrypt, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')

    carwashes = db.relationship('CarWash', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def logIn(self):
        # Pozwala użytkownikowi zalogować się do systemu.
        pass

    def changeAccountData(self):
        # Umożliwia użytkownikowi zmianę danych konta.
        pass

    def addCarWash(self, name, location):
        # Dodaje nową myjnię do systemu.
        carwash = CarWash(name=name, location=location, user_id=self.id)
        db.session.add(carwash)
        db.session.commit()

    def manageSchedule(self):
        # Zarządza harmonogramem zadań lub usług.
        pass

    def noteIncome(self):
        # Rejestruje dochody związane z usługami.
        pass

    def addChemicalsInventory(self):
        # Dodaje chemikalia do inwentarza.
        pass

    def reportChemicalAddition(self):
        # Raportuje dodanie chemikaliów do inwentarza.
        pass
class Admin(User):
    def addUser(self, username, email, password):
        # Dodaje nowego użytkownika do systemu.
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password, role='user')
        db.session.add(user)
        db.session.commit()

    def manageSchedule(self):
        # Zarządza harmonogramem zadań lub usług.
        pass

    def noteIncome(self):
        # Rejestruje dochody związane z usługami.
        pass

    def addChemicalsInventory(self):
        # Dodaje chemikalia do inwentarza.
        pass

    def reportChemicalAddition(self):
        # Raportuje dodanie chemikaliów do inwentarza.
        pass
class ExternalUser:
    def submitForm(self, formData):
        # Składanie formularza, prawdopodobnie do żądania usług lub zgłaszania problemów.
        pass
class CarWash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"CarWash('{self.name}', '{self.location}')"

    def addNewCarWash(self, name, location):
        # Dodaje nową myjnię.
        new_carwash = CarWash(name=name, location=location, user_id=self.user_id)
        db.session.add(new_carwash)
        db.session.commit()

    def manageSchedule(self):
        # Zarządza harmonogramem akcji myjni.
        pass

    def noteIncome(self):
        # Rejestruje dochody związane z usługami mycia samochodu.
        pass
class ChemicalsInventory:
    def addChemicals(self):
        # Dodaje chemikalia do inwentarza.
        pass

    def reportChemicalAddition(self):
        # Raportuje dodanie chemikaliów do inwentarza.
        pass
class InterfaceValidatorFormularza:
    def validate(self, formData):
        # Waliduje dane formularza przesłane przez zewnętrznego użytkownika.
        pass
class Raport:
    def createReport(self):
        # Tworzy raport.
        pass
class ObslugaRaportu:
    def assignToAdmin(self, report):
        # Przypisuje raport do obsługi przez administratora.
        pass

    def awaitApproval(self, report):
        # Oczekuje na zatwierdzenie raportu przesłanego przez zewnętrznego użytkownika.
        pass
