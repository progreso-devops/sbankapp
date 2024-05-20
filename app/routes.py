from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import SignUpForm, LoginForm
from app.models import User, Transaction

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, password=form.password.data,
                    branch_name=form.branch_name.data, mobile=form.mobile.data,
                    email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Sign up successful!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            flash('Login successful!', 'success')
            return redirect(url_for('profile', user_id=user.id))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    transactions = Transaction.query.filter_by(user_id=user.id).all()
    return render_template('profile.html', user=user, transactions=transactions)

@app.route('/add_transaction/<int:user_id>', methods=['POST'])
def add_transaction(user_id):
    from_account = request.form.get('from_account')
    to_account = request.form.get('to_account')
    remarks = request.form.get('remarks')
    transaction = Transaction(user_id=user_id, from_account=from_account, to_account=to_account, remarks=remarks)
    db.session.add(transaction)
    db.session.commit()
    flash('Transaction added!', 'success')
    return redirect(url_for('profile', user_id=user_id))

