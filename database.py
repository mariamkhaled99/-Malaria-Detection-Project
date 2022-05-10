
import mysql.connector
db=mysql.connector.connect(
    host="127.0.0.1",
   port="3308",
   user="root",
   passwd="",
   database="GenomicProject",
   autocommit=True
 )

mycursor=db.cursor()
# mycursor.execute("CREATE DATABASE GenomicProject ")
# mycursor.execute("CREATE TABLE Human_Genome_Indexed (k_mer varchar(250) , id int PRIMARY KEY AUTO_INCREMENT )")
# mycursor.execute("CREATE TABLE Plasmodium_falciparum_glutamic_protein (k_mer varchar(250) , id int PRIMARY KEY  )")

# mycursor.execute("CREATE TABLE Plasmodium_falciparum_glutamic_protein (k_mer varchar(250) ,position JSON ,id INT NOT NULL PRIMARY KEY AUTO_INCREMENT  )")
# mycursor.execute("CREATE TABLE Human_Genome_Chr9 (k_mer varchar(250) ,position JSON ,id INT NOT NULL PRIMARY KEY AUTO_INCREMENT  )")

# mycursor.execute("DROP TABLE Human_Genome_Chr9 ")

# mycursor.execute("DELETE FROM Plasmodium_falciparum_glutamic_protein ")
