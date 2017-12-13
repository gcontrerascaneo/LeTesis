handle = COM_OpenNXT('bluetooth.ini');
COM_SetDefaultNXT(handle);

disp('1.- Mover adelante');
disp('2.- Mover atras');
disp('3.- Mover derecha');
disp('4.- Mover Izquierda');
disp('5.- Cerrar');
opcion = input('Ingrese una opcion: ');
while opcion ~=5
    pause(0.000000000000001);
    switch opcion
        case 1
            NXT_StartProgram('MoverAdelante', handle);
            break;
        case 2
            NXT_StartProgram('MoverAtras', handle);
            break;
        case 3
            NXT_StartProgram('MoverDerecha', handle);;
            break;
        case 4
            NXT_StartProgram('MoverIzquierda', handle);
            break;
        case 5
            disp('Adios');
            COM_CloseNXT('all');
            break;
    end
end