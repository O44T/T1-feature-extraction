jpegFiles = dir('*.png');
numfiles = length(jpegFiles);
% numfiles = 10; %500;
Vertex = cell(1, numfiles);
% mydata = cell(1, numfiles);

fid = fopen('single_predictions.txt', 'rt');
C = textscan(fid, '%f%f%f%f%f%f', 'MultipleDelimsAsOne', true, 'Delimiter', ' ');
fclose(fid);
frame_col = cell2mat(C(3));
x_col = cell2mat(C(5));
y_col = cell2mat(C(4));
tic
% ------------------------------------------------------------------------
for frame_idx = 1:numfiles 

  FFC = imread(jpegFiles(frame_idx).name); 
  
  % [FF, ~] = imcrop(FFC,[0 600 900 100]);   
  % [FF, ~] = imcrop(FFC, [0 0 680 680]); 
  
%  F = im2bw(FFC); %imbinarize(F);
%  FR = imfill(F,8,'holes'); 
  % mydata2{1, k} = FR;
  
  
  % FR = imfill(im2bw(FFC),8,'holes');
  %FR = im2bw(FFC);
  FR = im2bw(~FFC);
  
  [row, col] = size(FR); 

  FR2 = zeros(row,col);
  
%% First filter

  for q = 2:col-1

    for r = 2:row-1
    
            if FR(r,q) == 0 
        
            Vx = [FR(r-1,q)   ; FR(r+1,q)   ; FR(r,q-1)   ; FR(r,q+1)   ; ...
                  FR(r-1,q-1) ; FR(r+1,q-1) ; FR(r-1,q+1) ; FR(r+1,q+1)];
               
                if numel(Vx(Vx == 0)) == 3
              
                    FR2(r,q) = 1;
                    
                end
                
            end   
            
    end
    
  end

%% Find vertex

  inde = find(FR2 == 1); 

  for ii = 1:size(inde,1)

    [iy,ix] = ind2sub(size(FR2),inde(ii));

    V(ii,1) = iy;
    V(ii,2) = ix;

  end

  pdispixel = zeros(size(inde,1),1);

  for ii = 1:size(inde,1)-1

    pdispixel(ii,1) = pdist2(V(ii,:),V(ii+1,:));

  end

  ii = 1;

  while ii < size(inde,1)
    
    if pdispixel(ii,1) > 2
        
        VV(ii,:) = V(ii,:);
        
    else
        
        VV(ii,1:2) = 0;
        
    end
    
    ii = ii + 1;
    
  end

  VV(VV(:,1)==0,:) = [];

%% Create a image of the vertices

% FRR = zeros(size(FR));

  [rows, columns] = size(FR);

  circleImage = false(rows, columns); 
  [x, y] = meshgrid(1:columns, 1:rows); 

  for ii = 1:size(VV,1)
    
    circleImage((x - VV(ii,2)).^2 + (y - VV(ii,1)).^2 <= 2^2) = true; 

  end

  s = regionprops(circleImage,'Centroid');
  centroidsvertex = cat(1,s.Centroid); 
  
  
  
  
  Vertex{1, frame_idx} = centroidsvertex; %Positions of bubble vertices 
  cell_to_mat = cell2mat(Vertex(1,frame_idx));
  
  imshow(jpegFiles.name)
  hold on
  plot(cell_to_mat(:,1), cell_to_mat(:,2),'o')
  
  
  
  
  newStr = split(jpegFiles(1,1).name, ["im", ".png"]);
  FrameNum = str2double(newStr(2,1));
  
  frame_idx = find(frame_col(:,1)==FrameNum);
  x_coord = x_col(frame_idx,1);
  y_coord = y_col(frame_idx,1);
  
  t1_mat = [x_coord; y_coord];
  
  vertex_matrix = cell2mat(Vertex(1));
  distance_vector = [];
  for i = 1:max(size(vertex_matrix))
       current_vertex = vertex_matrix(i,:);
       distance = norm(t1_mat - current_vertex.');
       distance1 = abs(t1_mat(1)-current_vertex(1));
       distance2 = abs(t1_mat(2)-current_vertex(2));
       if distance < 65
           distance_vector = [distance_vector; distance vertex_matrix(i,:)];
           plot(current_vertex(1), current_vertex(2),'o', 'Color', 'green')
       end
  end
  suspected_vertices = [];
  for j = 1:max(size(distance_vector))
      vertex_info1 = distance_vector(j,:);
      vertex_vector1 = [vertex_info1(2); vertex_info1(3)];
      for k = 1:max(size(distance_vector))
          vertex_info2 = distance_vector(k,:);
          vertex_vector2 = [vertex_info2(2); vertex_info2(3)];
          temp_dist = norm(vertex_vector1 - vertex_vector2);
          if temp_dist < 15 & temp_dist ~= 0
            dist_to_T1_1 = norm(t1_mat - vertex_vector1);
            dist_to_T1_2 = norm(t1_mat - vertex_vector2);
            if dist_to_T1_1 < dist_to_T1_2
                suspected_vertices = [suspected_vertices; vertex_info2];
            else
                suspected_vertices = [suspected_vertices; vertex_info1];
            end
          end
      end
  end
  
  unique_suspects = unique(suspected_vertices, 'rows', 'stable');
  %setdiff(unique_suspects, distance_vector,'rows');
  Lia = ismember(distance_vector, unique_suspects, 'rows');
  distance_vector_new = distance_vector(~Lia,:);
  plot(distance_vector_new(:,2), distance_vector_new(:,3),'o','Color','red')
  
  
  
  %atan2d(vec1(1)*vec2(2)-vec2(1)*vec1(2), vec1(1)*vec1(2)+vec2(1)*vec2(2));
  
  fileID = fopen('t1_loc.txt', 'w');
  formatSpec = '%4.2f %4.2f %4.2f A0 A1 A2 A3 A4 1';
  fprintf(fileID, formatSpec, FrameNum, x_coord, y_coord);
  fclose(fileID);
  
  
  
  
  
 
%% Clear variables
  
  clear FFC row col q FR2 r Vx VV ii ix iy ...
        rows columns circleImage x y centroidsvertex s ...
        k pdispixel V FR inde

end
toc