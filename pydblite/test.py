from pydblite import Base
db = Base('test.pydb') 
db.create('name', 'age', 'size') 
 
db.insert(name='homer', age=23, size=1.84) 
db.insert('homer', 23, 1.84)
db.commit() 
db.exists()