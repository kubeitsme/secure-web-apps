# Hash password
```python
plaintext = b"PASSWORD"
pepper = b"THIS_IS_PEPPER"
hpw = HashPassword(pepper)
password = hpw.create_hashed(plaintext)
if hpw.compare_hashed(plaintext, password):
  print("It Matches!")
else:
  print("It doesn't match")
```