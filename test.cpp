#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 0.0, 0.0); // set the color to red
    glLineWidth(3.0); // set the line width to 3.0 pixels

    // draw the heart shape using Bezier curves
    glBegin(GL_TRIANGLE_FAN);
        glVertex2f(0.0, 0.0);
        glVertex2f(-1.5, 1.0);
        glVertex2f(-3.0, 2.5);
        glVertex2f(-4.5, 1.0);
        glVertex2f(-4.5, -1.5);
        glVertex2f(-3.0, -3.0);
        glVertex2f(0.0, -4.5);
        glVertex2f(3.0, -3.0);
        glVertex2f(4.5, -1.5);
        glVertex2f(4.5, 1.0);
        glVertex2f(3.0, 2.5);
        glVertex2f(1.5, 1.0);
        glVertex2f(0.0, 0.0);
    glEnd();

    glFlush();
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Love Emoji");

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-5.0, 5.0, -5.0, 5.0, -1.0, 1.0);

    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
