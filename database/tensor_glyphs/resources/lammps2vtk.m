% Read dump file:
tensordata = "atoms.dump";
fileID = fopen(tensordata,'r');

% Skip header
fgetl(fileID);fgetl(fileID);fgetl(fileID);

% Get Number of Atoms
numOfAtoms = fscanf(fileID,'%d');

% Skip header
fgetl(fileID);fgetl(fileID);fgetl(fileID);fgetl(fileID);fgetl(fileID);

% Read data: id type x y z c1 c2 c3 c4 c5 c6
data = cell2mat(textscan(fileID,'%f %f %f %f %f %f %f %f %f %f %f'));
fclose(fileID);

% Positions and tensor data:
pos = data(:,3:5)';
tensor = data(:,6:end)';

% Write to VTK file:
vtkfilename = "atoms.vtk";
fileID = fopen(vtkfilename,'w');

% Write header:
fprintf(fileID,'# vtk DataFile Version 5.1\n');
fprintf(fileID,'LAMMPS to VTK\n');
fprintf(fileID,'BINARY\n');
fprintf(fileID,'DATASET UNSTRUCTURED_GRID\n');

fprintf(fileID,'POINTS %i FLOAT\n',numOfAtoms);
fwrite(fileID, pos, 'float','ieee-be');
fprintf(fileID,'\n');

fprintf(fileID,'POINT_DATA %i\n',numOfAtoms);
fprintf(fileID,'TENSORS6 STRESS float\n');
fwrite(fileID, tensor, 'float','ieee-be');

fclose(fileID);

