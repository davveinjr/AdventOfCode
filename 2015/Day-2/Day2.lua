-- Import file
file = io.open("input.txt", "r")
data = file:read("*a")
file:close()

-- Part 1
for line in data:gmatch("([^\n]*)\n?") do 
  -- Logic for Part 1
end

-- Part 2
for line in data:gmatch("([^\n]*)\n?") do 
  -- Logic for Part 2
end