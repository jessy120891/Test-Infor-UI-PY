## INFOR UI Tests

#### Requirements:
`pip install requirements.txt`

#### Run Tests:
`python -m pytest`

## Results:
![image](/runned_test_py.PNG)

#### Questions

##### Test case 1:
- open the web page
- open  www.booking.com
- Validate error message "Enter a destination to start searching." is showing.
- Validate destination input box shows "Where are you going?"
 
##### Test case 2:
- open  www.booking.com
- Click check in date and select today as check in
- Validate the date of yesterday is disabled
- Validate the date of today is disabled
- Select tomorrow as checkout day

