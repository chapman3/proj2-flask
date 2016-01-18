"""
Test program for pre-processing schedule
"""
import arrow
#import time

base = arrow.now()


#def calcWeek():
    #return time.strftime("%d/%m/%Y")


def weekComp(week):
    if week == 1:
        return "01/04/2016"
    elif week == 2:
        return "01/11/2016"
    elif week == 3:
        return "01/18/2016"
    elif week == 4:
        return "01/25/2016"
    elif week == 5:
        return "02/01/2016"
    elif week == 6:
        return "02/08/2016"
    elif week == 7:
        return "02/15/2016"
    elif week == 8:
        return "02/22/2016"
    elif week == 9:
        return "02/29/2016"
    elif week == 10:
        return "03/07/2016"


def process(raw):
    """
    Line by line processing of syllabus file.  Each line that needs
    processing is preceded by 'head: ' for some string 'head'.  Lines
    may be continued if they don't contain ':'.  
    """
    #currentDate = calcWeek()
    field = None
    entry = { }
    cooked = [ ] 
    for line in raw:
        line = line.rstrip()
        if len(line) == 0:
            continue
        parts = line.split(':')
        if len(parts) == 1 and field:
            entry[field] = entry[field] + line + " "
            continue
        if len(parts) == 2: 
            field = parts[0]
            content = parts[1]
        else:
            raise ValueError("Trouble with line: '{}'\n".format(line) + 
                "Split into |{}|".format("|".join(parts)))

        if field == "begin":
            try:
                base = arrow.get(content)
            except:
                raise ValueError("Unable to parse date {}".format(content))

        elif field == "week":
            if entry:
                cooked.append(entry)
                entry = { }
            #tempWeek = content.strip(" ")
            #entry['date'] = weekComp(tempWeek)
            #if currentDate >= entry['date'] and currentDate < weekComp(tempWeek+1):
                #entry['currentWeek'] = True
            #else:
                #entry['currentWeek'] = False
            print(content.format())
            entry['current_week'] = False
            entry['date'] = "test"
            entry['topic'] = ""
            entry['project'] = ""
            entry['week'] = content


        elif field == 'topic' or field == 'project':
            entry[field] = content

        else:
            raise ValueError("Syntax error in line: {}".format(line))

    if entry:
        cooked.append(entry)

    return cooked


def main():
    f = open("static/schedule.txt")
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()

    
    
            
    
