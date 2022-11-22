-- Import file
file = io.open("input.txt", "r")
data = file:read("*a")
file:close()

-- Step 1
p1Total = 0
for i = 1, #data do
  if data:sub(i,i) == "(" then p1Total = p1Total + 1 else p1Total = p1Total - 1 end
end

print(p1Total)
-- Step 2
p2Total = 0;
p2Tally = 1;

for i = 1, #data do
  if data:sub(i,i) == "(" then p2Total = p2Total + 1 else p2Total = p2Total - 1 end
  if p2Total == -1 then
    p2Tally = i
    break
  end
end

print(p2Tally)