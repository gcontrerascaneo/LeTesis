handle = COM_OpenNXT('bluetooth.ini');
COM_SetDefaultNXT(handle);
opcion = 0;
disp('1.- Mover adelante');
disp('2.- Mover derecha');
disp('3.- Mover izquierda');
disp('4.- Retroceder');
disp('5.- Cerrar');
while opcion ~=5
opcion = input('Ingrese una opcion: ');
    pause(0.000000000000001);
    switch opcion
        case 1
            if opcion == 1
                DirectMotorCommand(MOTOR_B, 60, 0, 'off', MOTOR_C, 0, 'off');
                pause(1);
                StopMotor(MOTOR_B, 'off');
                StopMotor(MOTOR_C, 'off');
            end
        case 2
            if opcion == 2
                DirectMotorCommand(MOTOR_B, 60, 90, 'off', MOTOR_A, 0, 'off');
                pause(1);
                StopMotor(MOTOR_B, 'off');
            end
        case 3
            if opcion == 3
                DirectMotorCommand(MOTOR_C, 60, 90, 'off', MOTOR_A, 0, 'off');
                pause(1);
                StopMotor(MOTOR_C, 'off');
            end
        case 4
            if opcion == 4
                DirectMotorCommand(MOTOR_B, -60, 0, 'off', MOTOR_C, -60, 'off');
                pause(1);
                StopMotor(MOTOR_B, 'off');
                StopMotor(MOTOR_C, 'off');
            end
        case 5
            if opcion == 5
                disp('Adios');
                COM_CloseNXT('all','bluetooth.ini');
                COM_CloseNXT('all');
            end
    end
end
