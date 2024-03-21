import pygame
import sys
import math
from copy import deepcopy


def arrow(screen, lcolor, tricolor, start, end, trirad, thickness=2):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi / 2
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                            end[1] + trirad * math.cos(rotation)),
                                           (end[0] + trirad * math.sin(rotation - 520),
                                            end[1] + trirad * math.cos(rotation - 520)),
                                           (end[0] + trirad * math.sin(rotation + 520),
                                            end[1] + trirad * math.cos(rotation + 520))))


t_and_p = {}


def save(rects, lines, circles):
    global t_and_p, flags
    t_and_l_in_p = {}
    for _ in range(len(rects)):
        lines_in_p = []
        for _1 in range(len(lines)):
            if rects[_][0] < lines[_1][0][0] < rects[_][2] and rects[_][1] < lines[_1][0][1] < rects[_][3]:
                lines_in_p.append([lines[_1][1], '+'])
            elif rects[_][0] < lines[_1][1][0] < rects[_][2] and rects[_][1] < lines[_1][1][1] < rects[_][3]:
                lines_in_p.append([lines[_1][0], '-'])
        t_and_l_in_p[f't{_ + 1}'] = lines_in_p
        for _1 in range(1, len(t_and_l_in_p) + 1):
            a = t_and_l_in_p[f't{_1}']
            local_list = []
            # print(a)
            for _2 in range(len(a)):
                p = a[_2]
                metks = []
                for _3 in range(len(circles)):
                    if circles[_3][0] < p[0][0] < circles[_3][2] and circles[_3][1] < p[0][1] < circles[_3][3]:
                        for _4 in range(len(flags)):
                            if circles[_3][0] < flags[_4][0] < circles[_3][2] and circles[_3][1] < flags[_4][1] < \
                                    circles[_3][3]:
                                metks.append(flags[_4])
                        local_list.append([circles[_3], p[1], metks])
            local_list.sort(key=lambda x: x[1], reverse=True)
            t_and_p[f't{_1}'] = local_list
            # print(local_list, end="\n\n\n\n")
            # print(local_list)
    # print('\n\n\n\n')
    # print(t_and_p)
    return t_and_p


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)
my_font2 = pygame.font.SysFont('Comic Sans MS', 30)
my_font3 = pygame.font.SysFont('Times New Roman', 50)
my_font4 = pygame.font.SysFont('Comic Sans MS', 50)

dis_width = 800
dis_height = 600
screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Сети Петри')
clock = pygame.time.Clock()


def main():
    global flags
    iter_now = 0
    screen.fill("black")
    flag_add_circle = False
    flag_add_rect = False
    flag_add_line = False
    flag_add_flag = False
    flag = True
    circles, rects, flags, lines = [], [], [], []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if pos[1] < 140:
                    if 100 < pos[0] < 180 and 25 < pos[1] < 105:
                        flag_add_circle = True
                        flag_add_rect = False
                        flag_add_line = False
                        flag_add_flag = False
                    elif 200 < pos[0] < 280 and 25 < pos[1] < 105:
                        flag_add_rect = True
                        flag_add_circle = False
                        flag_add_line = False
                        flag_add_flag = False
                    elif 300 < pos[0] < 380 and 25 < pos[1] < 105:
                        line1 = None
                        line2 = None
                        flag_add_line = True
                        flag_add_circle = False
                        flag_add_rect = False
                        flag_add_flag = False
                    elif 400 < pos[0] < 480 and 25 < pos[1] < 105:
                        flag_add_flag = True
                        flag_add_circle = False
                        flag_add_rect = False
                        flag_add_line = False
                    elif 0 < pos[0] < 60 and 0 < pos[1] < 60:
                        instruction()
                elif pos[1] > 140:
                    if flag_add_circle == True:
                        pygame.draw.circle(screen, "yellow", (pos[0], pos[1]), 25, 1)
                        circles.append([pos[0] - 25, pos[1] - 25, pos[0] + 25, pos[1] + 25])
                        text = my_font.render(f'P{len(circles)}', True, 'white')
                        screen.blit(text, ((pos[0] - 10, pos[1] - 60)))
                        # circles.append([pos[0]-25, pos[1]-25, 50, 50])
                        # pygame.draw.rect(screen, (255, 255, 255), (circles[0][0], circles[0][1], circles[0][2], circles[0][3]), 1)
                    elif flag_add_rect == True:
                        pygame.draw.rect(screen, 'cyan', (pos[0] - 12, pos[1] - 25, 20, 65), 1)
                        rects.append([pos[0] - 12, pos[1] - 25, pos[0] + 8, pos[1] + 40])
                        text = my_font.render(f'T{len(rects)}', True, 'white')
                        screen.blit(text, ((pos[0] - 15, pos[1] - 60)))
                        # rects.append([pos[0]-12, pos[1]-25, 20, 65])
                        # pygame.draw.rect(screen, (255, 255, 255), (rects[0][0], rects[0][1], rects[0][2], rects[0][3]), 1)
                    elif flag_add_flag == True:
                        pygame.draw.circle(screen, "white", (pos[0], pos[1]), 10, 0)
                        flags.append([pos[0], pos[1]])
                        # flags.append([pos[0]-10, pos[1]-10, 20, 20])
                        # pygame.draw.rect(screen, (255, 255, 255), (flags[0][0], flags[0][1], flags[0][2], flags[0][3]), 1)
                    elif flag_add_line == True:
                        if flag == True:
                            if line1:
                                line2 = pos
                                if line2:
                                    arrow(screen, 'white', 'white', line1, line2, 10, 2)
                                    lines.append([line1, line2])
                                    flag = False

                                    # pygame.draw.circle(screen, "white", lines[0][0], 10, 1)
                                    # pygame.draw.circle(screen, "white", lines[0][1], 10, 1)
                            line1 = pos
                        else:
                            flag = True
                            line1 = pos
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                elif event.key == pygame.K_RIGHT:
                    try:
                        counter = 0
                        counter_2 = 0
                        a = save(rects, lines, circles)
                        iter_now += 1
                        b = a[f't{iter_now}']
                        iter_dots = 0
                        max_iter_dots = len(b)
                        while iter_dots < max_iter_dots:
                            c = b[iter_dots]
                            if c[1] == '-':
                                counter_2 += 1
                                if len(c[2]) > 0:
                                    flags.remove(c[2][0])
                                    counter += 1
                            elif c[1] == '+' and (counter > 0 or counter_2 == 0):
                                flags.append([(c[0][0] + c[0][2]) / 2, (c[0][1] + c[0][3]) / 2])
                            a = save(rects, lines, circles)
                            '''pygame.draw.circle(screen, "black", ((c[0][0]+c[0][2])/2, (c[0][1]+c[0][3])/2), 25, 0)
                            pygame.draw.circle(screen, "yellow", ((c[0][0]+c[0][2])/2, (c[0][1]+c[0][3])/2), 25, 1)
                            pygame.draw.circle(screen, "white", ((c[0][0]+c[0][2])/2, (c[0][1]+c[0][3])/2), 10, 0)'''

                            iter_dots += 1
                            b = a[f't{iter_now}']
                    except:
                        main()
                    for _ in range(len(b)):
                        c = b[_]
                        if len(c[-1]) > 0:
                            pygame.draw.circle(screen, "black", ((c[0][0] + c[0][2]) / 2, (c[0][1] + c[0][3]) / 2), 25,
                                               0)
                            pygame.draw.circle(screen, "yellow", ((c[0][0] + c[0][2]) / 2, (c[0][1] + c[0][3]) / 2), 25,
                                               1)
                            pygame.draw.circle(screen, "white", ((c[0][0] + c[0][2]) / 2, (c[0][1] + c[0][3]) / 2), 10,
                                               0)

                            text = my_font.render(str(len(c[2])), True, 'black')
                            screen.blit(text, ((c[0][0] + c[0][2]) / 2 - 6, (c[0][1] + c[0][3]) / 2 - 15))
                        else:
                            pygame.draw.circle(screen, "black", ((c[0][0] + c[0][2]) / 2, (c[0][1] + c[0][3]) / 2), 25,
                                               0)
                            pygame.draw.circle(screen, "yellow", ((c[0][0] + c[0][2]) / 2, (c[0][1] + c[0][3]) / 2), 25,
                                               1)

        rect = pygame.Rect(100, 25, 80, 80)
        pygame.draw.rect(screen, 'white', rect, 2)
        pygame.draw.circle(screen, "yellow", (140, 65), 25, 1)

        rect = pygame.Rect(200, 25, 80, 80)
        pygame.draw.rect(screen, 'white', rect, 2)
        pygame.draw.rect(screen, 'cyan', (230, 35, 20, 60), 1)

        rect = pygame.Rect(300, 25, 80, 80)
        pygame.draw.rect(screen, 'white', rect, 2)
        arrow(screen, 'white', 'white', (340, 100), (340, 40), 10, 2)

        rect = pygame.Rect(400, 25, 80, 80)
        pygame.draw.rect(screen, 'white', rect, 2)
        pygame.draw.circle(screen, "white", (440, 65), 10, 0)

        text = my_font.render('позиция', True, 'white')
        screen.blit(text, ((100, -5)))
        text = my_font.render('переход', True, 'white')
        screen.blit(text, ((200, -5)))
        text = my_font.render('дуга', True, 'white')
        screen.blit(text, ((320, -5)))
        text = my_font.render('фишка', True, 'white')
        screen.blit(text, ((410, -5)))



        text = my_font.render('R — очистить', True, 'white')
        screen.blit(text, ((520, 20)))
        text = my_font.render('-> — следущая итерация', True, 'white')
        screen.blit(text, ((520, 50)))

        text = my_font3.render('?', True, 'white')
        screen.blit(text, ((20, 10)))

        pygame.display.update()


def instruction():
    screen.fill("black")

    rect = pygame.Rect(25, 25, 80, 80)
    pygame.draw.rect(screen, 'white', rect, 2)
    text = my_font4.render('<-', True, 'white')
    screen.blit(text, ((48, 25)))

    text = my_font.render('Эмулятор сетей Петри', True, 'white')
    screen.blit(text, ((400, 25)))

    text = my_font.render('Сначала нужно выбрать, какой объект вы хотите создать и нажать', True, 'white')
    screen.blit(text, ((120, 80)))
    text = my_font.render('соответствующую кнопку (входные и выходные позиции, переходы,  ', True, 'white')
    screen.blit(text, ((120, 100)))
    text = my_font.render('фишки). Для смены выбора нажмите на другую кнопку.', True, 'white')
    screen.blit(text, ((120, 120)))

    text = my_font.render('Далее нажмите на область, в которую хотите поместить объект.', True, 'white')
    screen.blit(text, ((120, 160)))
    text = my_font.render('Для расположения стрелки нужно нажать дважды: в начало и конец', True, 'white')
    screen.blit(text, ((120, 180)))
    text = my_font.render('стрелки. Границы стрелок должны находиться внутри какого-либо', True, 'white')
    screen.blit(text, ((120, 200)))
    text = my_font.render('объекта.', True, 'white')
    screen.blit(text, ((120, 220)))

    text = my_font.render('Для запуска сети нажмите стрелку вправо (->). Это запустит', True, 'white')
    screen.blit(text, ((120, 260)))
    text = my_font.render('первую итерацию. Для следущей итерации нажмите стрелку еще раз.', True, 'white')
    screen.blit(text, ((120, 280)))
    text = my_font.render('Количество возможных итераций равно количеству переходов.', True, 'white')
    screen.blit(text, ((120, 300)))
    text = my_font.render('Когда итерации закончатся, экран очистится, и вы сможете создать', True, 'white')
    screen.blit(text, ((120, 320)))
    text = my_font.render('ещё одну сеть Петри.', True, 'white')
    screen.blit(text, ((120, 340)))

    text = my_font.render('Для очистки экрана нажмите клавишу "R" на клавиатуре.', True, 'white')
    screen.blit(text, ((120, 380)))



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if 25 < pos[0] < 105 and 25 < pos[1] < 105:
                    main()
        pygame.display.update()


main()

'''
t1 = [-p1, +p2, +p3]
t2 = [-p3, -p2, +p2, +p4]
t3 = [-p3, -p4 -p1]
'''

# {'t1': [[[96, 356, 146, 406], '-']], 't2': [[[96, 356, 146, 406], '-'], [[362, 377, 412, 427], '+']]}


'''
{'t1': [[[106, 335, 156, 385], '-', 2]], 
't2': [[[106, 335, 156, 385], '-', 2], [[397, 408, 447, 458], '+', 0]]}
'''
