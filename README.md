# Curiosa
Django Based Blogging Web Application
Key Features:
1) Blogs Belongs to a Category:
Each Blog has a parent class, Category Class. This makes it easier to group blogs and decide what type of content it consists. On creation or deletion of the Category. All blogs who belongs to it gets wiped out. 
   ![Screenshot 2023-07-22 214244](https://github.com/shivamtherexpandey/Curiosa/assets/95215534/96b1ad67-b3f1-42c6-bf60-96210fb0c4bf)

2) View based Recommendation:
Blogs with the highest views belongs to the Popular blogs group in Sidebar. Similarily, Categories with highest views are also presented on Top of Sidebar. This recommendation could be altered by the admin.
![Screenshot 2023-07-22 215422](https://github.com/shivamtherexpandey/Curiosa/assets/95215534/b2e12c14-f649-410c-b7a8-076966ee40e3)

3) Present Content of Blog With Image:
Blogs are stored with images to express the ideas and concepts of the blog in a better way. Each blog can have images to express the writer's point of view. These images are stored in the MEDIA folder and are maintained using ImageField() in Models.
![Screenshot 2023-07-22 221143](https://github.com/shivamtherexpandey/Curiosa/assets/95215534/36cc28fa-8bfb-4eff-a550-22e8e0c58094)

![Screenshot 2023-07-22 221456](https://github.com/shivamtherexpandey/Curiosa/assets/95215534/02479b9e-bd43-486d-b945-370201da5347)

4) Edit Content With Django SummerNote Editor:
Web Application makes use of SummerNote Editor to shape the content of the blog to make it more presentable. Adding bold text, hyperlink, Adding Table, Image and Video on the content of the blog.
![Screenshot 2023-07-22 222447](https://github.com/shivamtherexpandey/Curiosa/assets/95215534/8eca55bd-168f-4f96-b2c6-a540372858f8)

5) Custom Django Admin Panel:
Curiosa has custom admin panel which is more presentable and attractive than Django Admin Panel. This custom admin panel makes use of django-material-admin.
![Screenshot 2023-07-22 223257](https://github.com/shivamtherexpandey/Curiosa/assets/95215534/39f57112-9149-42fc-a8b1-82ee74b39df1)

 
