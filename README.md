* Name: Tirza Gabriella
* Nim: 2602109870
* B26 L1AC


# cara 1
## input
```
print(file.readlines())
```

## output
```
['halo\n', 'guys\n', 'ini\n', 'cuma\n', 'contoh\n', 'buat\n', 'tugas\n', 'ko\n', 'alvin\n', 'hehe']
```

# cara 2
## input
```
listStatement = []

for f in file.readlines():
  listStatement.append(f.rstrip())

print(listStatement)
```
in here rstip is used to delete "\n" (enter)

## output
```
['halo', 'guys', 'ini', 'cuma', 'contoh', 'buat', 'tugas', 'ko', 'alvin', 'hehe']
```
