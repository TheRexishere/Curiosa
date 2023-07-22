from django.shortcuts import render, HttpResponse
from BloggingApp.models import Blog, Category

# Create your views here.

def get_processed_data():
    # Accessing the Categories
    categories = Category.objects.all()

    # Accessing 5 Popular categories
    popular_categories = Category.objects.all().order_by('-cat_view_count', '-date_of_creation')[:5:]

    # Accessing 5 Popular Posts
    popular_post = Blog.objects.all().order_by('-blog_view_count', '-date_of_creation')[:5:]

    # Accessing 5 Recent Blogs
    recent_blogs = Blog.objects.all().order_by('-blog_id')[:5:]

    return categories, popular_categories, popular_post, recent_blogs

def home(request):
    '''Extract Blogs Content from the database and
     generate the Webpage as response'''

    # Accessing the Blogs up to 5 Post
    blogs = Blog.objects.all().order_by('blog_id')[:5:]

    categories, popular_categories, popular_post, recent_blogs = get_processed_data()

    #print(blogs)

    page_nums = {'first': 1, 'second': 2}

    blog_data = {
        'articles': blogs,
        'categories': categories,
        'popular_categories': popular_categories,
        'popular_post': popular_post,
        'recent_blogs': recent_blogs,
        'page_numbers': page_nums,
    }

    return render(request, 'index.html', blog_data)


def show_blog(request, blog_url):
    ''' Load selected blog content using
    the blog url requested '''

    # Accessing the Blog
    blog = Blog.objects.get(blog_url=blog_url)
    blog.blog_view_count += 1
    blog.category.cat_view_count += 1

    # Save Changes to Blog
    blog.save()

    # Save Changes to Category
    blog.category.save()

    categories, popular_categories, popular_post, recent_blogs = get_processed_data()

    # print(blog.category.cat_view_count)

    blog_data = {
        'article': blog,
        'categories': categories,
        'popular_categories': popular_categories,
        'popular_post': popular_post,
        'recent_blogs': recent_blogs,
    }

    return render(request, 'blog.html', blog_data)


def show_category(request, cat_URL):
    ''' Load all the Categories in the
    database to show blog category wise'''

    categories, popular_categories, popular_post, recent_blogs = get_processed_data()

    # Selecting Requested Category
    category = Category.objects.get(cat_URL=cat_URL)
    category.cat_view_count += 1

    # Save changes to Category
    category.save()

    blog = Blog.objects.filter(category=category)

    if len(blog) > 5:
        page_nums = {'first':1, 'second':2}
    else:
        page_nums = {'first':1}
        first_only_page = True

    last_page = False

    blog_data = {
        'articles': blog,
        'categories': categories,
        'category': category,
        'popular_categories': popular_categories,
        'popular_post': popular_post,
        'recent_blogs': recent_blogs,
        'page_numbers': page_nums,
        'last': last_page,
        'first': first_only_page,
    }


    return render(request, 'category.html', blog_data)

def load_cat_page(request, cat_URL, page_num):
    category = Category.objects.get(cat_URL=cat_URL)
    #print(category)
    all_blogs = Blog.objects.filter(category=Category.objects.get(cat_URL=cat_URL))

    if page_num != 0 and len(all_blogs) > 5 * (page_num-1):
        blog = all_blogs[5*(page_num-1):5*(page_num-1)+5:]

        #print(blog)

        categories, popular_categories, popular_post, recent_blogs = get_processed_data()

        last_page = False

        if page_num != 1:
            page_nums = { 'second':page_num}
            if len(all_blogs) > 5 * (page_num):
                page_nums['third'] = page_num+1
            else:
                last_page = True
        else:
            page_nums = { 'first': page_num, 'second':page_num+1}

        blog_data = {
            'articles': blog,
            'categories': categories,
            'category': category,
            'popular_categories': popular_categories,
            'popular_post': popular_post,
            'recent_blogs': recent_blogs,
            'page_numbers': page_nums,
            'last': last_page,
        }

        return render(request, 'category.html', blog_data)
    else:
        return HttpResponse("Error 404 : Page Not Found!")

def load_page(request, page_num):
    all_blogs = Blog.objects.all()


    if page_num != 0 and len(all_blogs) > 5 * (page_num-1):
        blog = all_blogs[5*(page_num-1):5*(page_num-1)+5:]

        #print(blog)

        categories, popular_categories, popular_post, recent_blogs = get_processed_data()

        last_page = False

        if page_num != 1:
            page_nums = { 'first': page_num-1, 'second':page_num}
            if len(all_blogs) > 5 * (page_num):
                page_nums['third'] = page_num+1
            else:
                last_page = True
        else:
            page_nums = { 'first': page_num, 'second':page_num+1}

        blog_data = {
            'articles': blog,
            'categories': categories,
            'popular_categories': popular_categories,
            'popular_post': popular_post,
            'recent_blogs': recent_blogs,
            'page_numbers': page_nums,
            'last': last_page,
        }

        return render(request, 'index.html', blog_data)
    else:
        return HttpResponse("Error 404 : Page Not Found!")

