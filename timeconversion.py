#!/usr/bin/py
from datetime import datetime
 
def convertToEuTime(us_time):
    return datetime.strptime(us_time, '%I:%M:%S%p').strftime('%H:%M:%S')
 
if __name__ == '__main__':
    us_time = raw_input()
    print convertToEuTime(us_time)
    use std::io;
 
fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).ok().expect("Failed to read line");
     
    let a: String = line.chars().skip(0).take(2).collect();
    let b: String  = line.chars().skip(3).take(2).collect();
    let c: String  = line.chars().skip(6).take(2).collect();
    let d: String  = line.chars().skip(8).take(2).collect();
     
    let a = a.trim().parse::<u32>().unwrap();
    let b = b.trim().parse::<u32>().unwrap();
    let c = c.trim().parse::<u32>().unwrap();
     
    let a = (a % 12) + match d.as_ref()  {
        "AM"    => 0,
        "PM"    => 12,
        _       => panic!("Unknown date type"),
    };
     
    println!("{:02}:{:02}:{:02}", a, b, c);
}




# Python program to convert time
# from 12 hour to 24 hour format

# Function to convert the date format
def convert24(str1):
	
	# Checking if last two elements of time
	# is AM and first two elements are 12
	if str1[-2:] == "AM" and str1[:2] == "12":
		return "00" + str1[2:-2]
		
	# remove the AM	
	elif str1[-2:] == "AM":
		return str1[:-2]
	
	# Checking if last two elements of time
	# is PM and first two elements are 12
	elif str1[-2:] == "PM" and str1[:2] == "12":
		return str1[:-2]
		
	else:
		
		# add 12 to hours and remove PM
		return str(int(str1[:2]) + 12) + str1[2:8]

# Driver Code		
print(convert24("08:05:45 PM"))
