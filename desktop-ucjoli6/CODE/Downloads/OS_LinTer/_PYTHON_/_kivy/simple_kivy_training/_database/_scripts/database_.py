# import os
import sqlite3 as sql_

# ----------------------------------------------------------------------------------------------------------------------
class SQLQuery(str):
  pass
# -----------------------------
class AppDatabase:
  """
  **Database Handler (manager) for my tiny App example**
  - *Reuseability* Guaranted
  """

  def __init__(self, filePath:str=None, ):
    self.filepath_ = filePath
  
  """def _global_(self, ):
    global conn_
    global cursor_"""
  
  def _connect2database_(self, datasase_filePath:str=None,
                        ):
    if not datasase_filePath:
      if self.filepath_:
        datasase_filePath == self.filepath_
    #
    global conn_
    try:
      conn_ = sql_.connect(
        database=datasase_filePath,
      )
    except FileNotFoundError as FNFE:
      FNFE.strerror
    except TypeError as TE:
      TE.args
  
  def _init_database_(self, ):
    global cursor_
    cursor_ = sql_.Cursor(conn_)
    # CREATING TABLE user_
    cursor_.execute("DROP TABLE IF EXISTS user_;")
    cursor_.execute(
      """
      CREATE TABLE IF NOT EXISTS user_ (
        userID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
        lastName TEXT NOT NULL,
        firstName TEXT NOT NULL,
        age INTEGER NOT NULL,
        birthDate DATE,
        birthPlace TEXT NOT NULL,
        residencePlace TEXT NOT NULL,
        height INTEGER NOT NULL,
        weigth INTEGER NOT NULL,
        morphology TEXT,
        defects TEXT,
        isTerrian TEXT
      );
      """
    )
    
  def _queryDatabase_(self, sqlQuery_:SQLQuery|str):
    response_ = cursor_.execute(
      sqlQuery_
    )
    return response_

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  appDB = AppDatabase()
  appDB._connect2database_(datasase_filePath="..\\app_database_.db")
  appDB._init_database_()

  # QUERIES HERE
  cursor_.executemany(
    "insert into user_ (lastName, firstName, age, birthDate, birthPlace, residencePlace, height, weigth, morphology, defects, isTerrian) \
      values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    [
      ('Uzumaki', 'Naruto', 31, '1994-02-21', 'Konoha', 'Konoha', 185, 54.3, "['pretentious', 'repetitive']", "['host', 'expensive chakra']", 'True'),
      ('Uchiha', 'Sasuke', 32, '1993-02-14', 'Konoha', 'Konoha', 182, 51.0, "['marked', 'possessed']", "['dark', 'lost', 'worrying', 'desperate']", 'True'),
      ('.', 'Toneri', 29, '1997-06-17', 'Konoha', '.', 171, 47.6, "['transferred']", "['dark', 'sharp', 'moon']", 'False'),
    ]
  ) # not cursor_.execute([] || (),(),(),...)
  #
  print(f"\n{ "-"*100 }")
  response_ = cursor_.execute(
    "SELECT * FROM user_"
  )
  print(f" { response_.fetchone() } ")
  print(f"{ "-"*100 }\n")
  print("With loop for ... in ...:..., we got: ")
  for row_ in response_:
    print(f"-> {row_}")
  print(f"{ "-"*100 }\n")
  #
  conn_.commit()
  cursor_.close()

