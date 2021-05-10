import curses


def my_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    _input = stdscr.getstr(r + 1, c, 20).decode('utf-8')
    return _input


def CourseName(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_name()
   


def CourseCredit(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_credit()
    
