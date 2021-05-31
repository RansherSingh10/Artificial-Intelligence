from pyDatalog import pyDatalog

# pyDatalog.create_terms('father,name1,name2')

pyDatalog.create_terms("father","cousin","grandchild","brother",'X','Y','Z','W')

#unification

+father('Bardock','Goku')
+father('Goku','Gohan')
+father('Goku','Goten')
+father('Raditz','Raunch')
+father('Bardock','Raditz')
+father('Gohan','Pan')


brother(X,Y)<=(father(Z,X) & father(Z,Y) & ~(X==Y))
cousin(X,Y)<=(father(Z,X) & father(W,Y) & brother(Z,W))
grandchild(X,Y)<=(father(Z,X) & father(Y,Z))

#resolution

print('Brother:')
print(brother(X,Y))
print('\nCousin:')
print(cousin(X,Y))
print('\nGrandchild:')
print(grandchild(X,Y))



pyDatalog.create_terms("wife","spouse","daughter","female","male", 'A', 'B', 'C')

+wife("Bulma","Vegeta")
+spouse("Vegeta","Bulma")
+daughter("Bulla","Vegeta")


female(A) <= ( wife(A, B) )
female(A) <= (daughter(A, B) )
male(A)  <= spouse(A, B)
daughter(A,C) <= (daughter(A, B) & wife(C, B) )


print('\n\nCheck if Bulla is a female')
print(bool(female("Bulla")))

print('Check if Bulla is a male')
print(bool(male("Bulla")))

print("List all the Females")
print(female(A))

print("Check if Bulla is a daughter of Bulma")
print(bool(daughter("Bulla","Bulma")))