class Validator:
  @staticmethod
  def is_valid_email(email):
    return "@" in email and "." in email
print(Validator.is_valid_email("abc@gmailcom"))