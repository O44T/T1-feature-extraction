jpegFiles = dir('*.jpg'); 
numfiles = length(jpegFiles);
% numfiles = 10; %500;
Vertex = cell(1, numfiles);
% mydata = cell(1, numfiles);
tic
% ------------------------------------------------------------------------
for k = 1:numfiles 

  FFC = imread(jpegFiles(k).name); 
  
  % [FF, ~] = imcrop(FFC,[0 600 900 100]);   
  % [FF, ~] = imcrop(FFC, [0 0 680 680]); 
  
%  F = im2bw(FFC); %imbinarize(F);
%  FR = imfill(F,8,'holes'); 
  % mydata2{1, k} = FR;
  
  
  % FR = imfill(im2bw(FFC),8,'holes');
  FR = im2bw(FFC);
  
  
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

  Vertex{1, k} = centroidsvertex; %Positions of bubble vertices 

%% Clear variables
  
  clear FFC row col q FR2 r Vx VV ii ix iy ...
        rows columns circleImage x y centroidsvertex s ...
        k pdispixel V FR inde

end
toc