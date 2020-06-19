import csv

states = [
    { "name": "California", "population": "39,512,223" },
    { "name": "Texas", "population": "28,995,881" },
    { "name": "Florida", "population": "21,477,737" },
    { "name": "New York", "population": "19,453,561" },
    { "name": "Pennsylvania", "population": "12,801,989" },
    { "name": "Illinois", "population": "12,671,821" },
    { "name": "Ohio", "population": "11,689,100" },
    { "name": "Georgia", "population": "10,617,423" },
    { "name": "North Carolina", "population": "10,488,084" },
    { "name": "Michigan", "population": "9,986,857" },
    { "name": "New Jersey", "population": "8,882,190" },
    { "name": "Virginia", "population": "8,535,519" },
    { "name": "Washington", "population": "7,614,893" },
    { "name": "Arizona", "population": "7,278,717" },
    { "name": "Massachusetts", "population": "6,949,503" },
    { "name": "Tennessee", "population": "6,833,174" },
    { "name": "Indiana", "population": "6,732,219" },
    { "name": "Missouri", "population": "6,137,428" },
    { "name": "Maryland", "population": "6,045,680" },
    { "name": "Wisconsin", "population": "5,822,434" },
    { "name": "Colorado", "population": "5,758,736" },
    { "name": "Minnesota", "population": "5,639,632" },
    { "name": "South Carolina", "population": "5,148,714" },
    { "name": "Alabama", "population": "4,903,185" },
    { "name": "Louisiana", "population": "4,648,794" },
    { "name": "Kentucky", "population": "4,467,673" },
    { "name": "Oregon", "population": "4,217,737" },
    { "name": "Oklahoma", "population": "3,956,971" },
    { "name": "Connecticut", "population": "3,565,287" },
    { "name": "Utah", "population": "3,205,958" },
    { "name": "Iowa", "population": "3,155,070" },
    { "name": "Puerto Rico", "population": "3,193,694" },
    { "name": "Nevada", "population": "3,080,156" },
    { "name": "Arkansas", "population": "3,017,825" },
    { "name": "Mississippi", "population": "2,976,149" },
    { "name": "Kansas", "population": "2,913,314" },
    { "name": "New Mexico", "population": "2,096,829" },
    { "name": "Nebraska", "population": "1,934,408" },
    { "name": "Idaho", "population": "1,787,065" },
    { "name": "West Virginia", "population": "1,792,147" },
    { "name": "Hawaii", "population": "1,415,872" },
    { "name": "New Hampshire", "population": "1,359,711" },
    { "name": "Maine", "population": "1,344,212" },
    { "name": "Montana", "population": "1,068,778" },
    { "name": "Rhode Island", "population": "1,059,361" },
    { "name": "Delaware", "population": "973,764" },
    { "name": "South Dakota", "population": "884,659" },
    { "name": "North Dakota", "population": "762,062" },
    { "name": "Alaska", "population": "731,545" },
    { "name": "District of Columbia", "population": "705,749" },
    { "name": "Vermont", "population": "623,989" },
    { "name": "Wyoming", "population": "578,759" },
    { "name": "Guam", "population": "165,718" },
    { "name": "U.S. Virgin Islands", "population": "104,914" },
    { "name": "American Samoa", "population": "55,641" },
    { "name": "Northern Mariana Islands", "population": "55,194" },
]

file_name = "states.csv"

with open(file_name, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "population"])
    writer.writeheader()
    writer.writerows(states)