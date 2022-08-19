# -*- coding: utf-8 -*-
from math_utils.point import Point
from math_utils.angle import degrees

# El rol "BallFollower" sigue ciegamente a la pelota.
# ¡Ojo que podemos meter goles en contra! 
class BallFollower:
    def applyOn(self, robot, snapshot):
        # Si sabemos dónde está la pelota, nos movemos hacia ella.
        # Caso contrario, nos movemos al centro de la cancha
        if snapshot.ball != None:
            ball = snapshot.ball.position
            if snapshot.color == "Y":
                if ball.y > -0.35:
                    robot.moveToBall()
            else:
                if ball.y < 0.35:
                    robot.moveToBall()
        else:
            robot.moveToPoint(Point(-0.2,0))

class BallFollower2:
    def applyOn(self, robot, snapshot):
        # Si sabemos dónde está la pelota, nos movemos hacia ella.
        # Caso contrario, nos movemos al centro de la cancha
        if snapshot.ball != None:
            ball = snapshot.ball.position
            if snapshot.color == "Y":
                if ball.y > -0.35:
                    robot.moveToBall()
                else:
                    robot.moveToPoint(Point(0.2,-0.1))
            else:
                if ball.y < 0.35:
                    robot.moveToBall()
                else:
                     robot.moveToPoint(Point(0.2,0.1))
        else:
            if snapshot.color == "Y":
                robot.moveToPoint(Point(0.2,-0.1))
            else:
                robot.moveToPoint(Point(0.2,+0.1))

# El rol "Goalkeeper" implementa un arquero básico
class Goalkeeper: 
    def applyOn(self, robot, snapshot):
        # Definimos un punto objetivo en el cual queremos ubicar el robot.
        # Este punto está dado por la coordenada X de la pelota y un valor
        # de Y fijo (este valor está definido de forma que esté cerca del 
        # arco pero fuera del área)
        if snapshot.ball != None:
            ball = snapshot.ball.position
        else:
            ball = Point.ORIGIN

        # Si el robot está lo suficientemente cerca del punto objetivo, 
        # entonces giramos para mirar a los laterales. Sino, nos movemos
        # hacia el punto objetivo
        if snapshot.color == "Y":
                target = Point(ball.x, - 0.65)
        else:
                target = Point(ball.x,+ 0.65)
        posicion= robot.getPosition()
        dist = abs(posicion.y-ball.y) 
        print(dist)
        if dist < 0.1:
            if snapshot.color == "Y":
                robot.lookAtAngle(degrees(180))             
                target = Point(ball.x, ball.y+0.05)
                robot.moveToPoint(target)            
            else:
                robot.lookAtAngle(degrees(0))              
                target = Point(ball.x, ball.y-0.05)
                robot.moveToPoint(target)             
        else:
            robot.moveToPoint(target)