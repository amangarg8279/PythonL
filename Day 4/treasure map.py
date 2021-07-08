r1=["😒","😒","😒"]
r2=["😒","😒","😒"]
r3=["😒","😒","😒"]
all_row_=[r1,r2,r3]
print(f"{r1}\n{r2}\n{r3}\n")
vals=(input("please select row where you want replace Row and colum"))
hori=int(vals[0])
vert=int(vals[1])
selected_row=all_row_[vert-1]
selected_row[hori-1]="X"
print(f"{r1}\n{r2}\n{r3}\n")