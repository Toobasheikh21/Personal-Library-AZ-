# # Library 


# import streamlit as st # import streamlit
# import json # import json
# import os 
# import random
# from datetime import datetime

# st.set_page_config(
#     page_title="✡AZ Pesonal Library Manger",
#     page_icon="📃",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # CSS Style
# st.markdown(
#     """
#       <style>
#           .welcome-banner {
#              background:liner-gradient(135deg, #6366f1, #4f46e5);
#              color:white;
#              padding:2rem;
#              border-top-right-radius:12px;
#              border-top-left-radius:12px;
          
#           }
#           h1,h2,h3 {
#           text-align:center;
#           margin-bottom:1rem;
#           }
          
#     .stButton > button {
#           width:100;
#           border-radius:8px;
#           font-weight:500;
#           color:white;
#           height:2.75rem;
#           }

#           .primary-button {
#                background:liner-gradient(135deg, #6b7280, #4b5563) !important;
#           }

#           .secondary-btn {
#                 background:liner-gradient(135deg, #f59e0b, #d97706) !important;
#           }
#           .danger-btn {
#               background:liner-gradient(135deg, #ef4444, #dc2626,) ! important;
#               }
#           .book-card {
#              background:liner-gradient(135deg, rgb(219, 229, 239), rgb(195, 219, 231, ), rgb(234, 237,239)) !important;
#              color:rgb(249, 249, 249);
#              border-radius:12px;
#              padding:1.5rem;
#              margin-bottom:1.5rem;
#              box-shadow:0 4px 12px  rgba(0, 0, 0.05);
#           }
#           .book-card.read-card {
#               border-left:6px solid #10b981;
#               border-right:6px solid #10b981;
#           }
#           .book-card.unread-card {
#              border-left:6px solid #6366f1;
#              border-right:6px solid #6366f1;
          
#           }
#           .state-card {
#              background:liner-gradient(135deg, rgb(253, 253, 253), rgba(195, 219, 231), rgb(255, 255, 255)) !important;
#              padding:1.5rem;
#              border-radius:12px;
#              box-shadow:0 4px 12px rgba(0, 0, 0.05);
#              text-align:center;
#              margin-bottom: 1.5rem;
#             }
#              .state-icon {
#                 font-size: 2.5rem;
#                 margin-bottom: 0.5rem;
#                 color: #6b7280;
#                 }
#                 .state-value {
#                     font-size: 2rem;
#                     font-weight: 600;
#                     color: #1f2937;
#                 }
#                   .state-title {
#                       font-size:1rem;
#                       color: #6b7280;
#                 }
#                 .stTabs [data-baseweb="tab-list"]{
#                      gap:1rem;
#                      padding:0.5rem;
#                      background:white;
#                      border-bottom-right-radius: 12px;
#                      border-bottom-left-radius:  12px;

#                 }
#                 .stTans [data-baseweb="tab"] {
#                     border-radius:8px;
#                     padding:1rem 1.5rem
#                     font-weight:500;
#                     color:rgb(0,0,0);

#                     transition:all 0.3s ease;
                
#                 }
#                 .stTabs [aria-selected="true"] {
#                     background: #6366f1;
#                     color:white;
#                     box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
#                 }
#                 .stTabs [data-base="tab"]:hover {
#                     color: #4b5563;;
#                 }

#                 .stTextInput > div > div > input, 
#                 .stSelectbox > div > div > div:focus {
#                    border-color : #6366f1;
#                    box-shadow:0 0 0 3px rgba(99, 102, 241, 0.1);
#                 }
#                    .search-bar {
#                        background:white;
#                        padding: 1.5rem;
#                        border-radius: 12px;
#                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
#                    }
#                    .book-title {
#                       font-size: 1.25rem;
#                       font-weight: 600;
#                       color: #1f2937;
#                    }
#                    .book-meta {
#                       color: #6b7280;
#                       fon-size: 0.95rem;
#                    }
#                    .status-badge {
#                       padding: 0.25rem 0.27rem;
#                       border-radius: 9999px;
#                       font-size: 0.875rem;
#                       font-weight:500;
#                    }
#                    .read-badge {
#                       background: #d1fae5;
#                       color: #065f46;
#                    }
#                    .unread-badge {
#                       background: #e0e7ff;
#                       color #4338ca;
#                    }
#                    .footer {
#                       text-align: center;
#                       padding: 2rem 0;
#                       color: #9ca3af;
#                       border-top: 1px solid #e5e7eb;
#                       margin-top: 3rem;
#                       font-size: 19px;
#                       font-weight:500;
#                    }
#                    .empty-state {
#                      text-align:center;
#                      padding: 4rem;
#                      color: #6b7280;
#                    }
#                    .empty-icon {
#                       font-size: 4rem;
#                       margin-bottom:1rem;
#                    }

#       </style>
# """, unsafe_allow_html=True
# )
# def load_library():
#     if os.path.exists("library.json"):
#         try:
#             with open("library.json","r") as file:
#                 return json.load(file)
#         except json.JSONDecodeError:
#             st.error("Error loading libray file. Starting with an empty library:")
#         return[]
    
# def save_library(library):
#     with open("library.json","w") as file:
#         json.dump(library,file,indent=4)
#         return True
    
# if "library" not in st.session_state:
#     st.session_state.library = load_library()

# def add_book(title,author,year,gnre,read_status):
#     if not title or author:
#         st.error("Title and Author are Required:")
#         return False
    
#     try:
#         year = int(year)
#         if not (1000 <=year <= datetime.now().year):
#             st.error(f"Year must be between 1000 and {datetime.now().year}:")
#             return False
#     except ValueError:
#         st.error("Year must be a valid Number:")
#         return False
    

#     book = {
#         "id":str(random,randint(10000,99999)), # type: ignore
#         "title":title,
#         "author":author,
#         "year":year,
#         "genre":gnre,
#         "read":read_status,
#         "date_added":datetime.now().strftime("%Y-%m-%d")
#     }
#     st.session_state.library.append(book)
#     save_library(st.session_state.library)
#     return True


# def remove_book(book_id):
#     for i, book in enumerate(st.session_state.library):
#         if book["id"] == book_id:
#             del st.session_state.library[i]
#             save_library(st.session_state.library)
#             return True
#         return False
    



#     def toggle_read_status(book_id):
#         for book in st.session_state.library:
#             if book["id"] == book_id:
#                 book["read"] = not book["read"]
#                 save_library(st.session_state.library)
#                 return True
#             return False
        

#     def search_books(search_term, search_by):
#         search_term = search_term.lower()
#         return[book for book in st.session_state.library
#                if search_term in book[search_by].lower()]
    

#     def get_statistics():
#         total_books = len(st.session_state.library)
#         read_books = sum(1 for book in st.session_state.library if book["read"])
#         percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
#         return{
#             "total":total_books,
#             "read":read_books,
#             "unread":total_books - read_books,
#             "percentage": percentage_read
#         }
    


#     st.markdown(
#         """
#          <div class="welcome-banner">
#               <h1 style="font-size:24px; text-align:center:">✡AZ Pesonal Library Manger</h1>
#         </div>
#        """,
#        unsafe_allow_html=True
#     )


#     tabs = st.tabs(["📚 Library","+Add Book","🏸Search","🚠Insights:"])


#     with tabs[0]:
#         st.header("🚋My Library")
#         with st.container():
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 filter_status = st.selectbox("Status",["All","Read","Unread"])

#             with col2:
#                 genres = ["All"] + sorted(list({book["genre"] for book in st.session_state.library}))
#                 filter_genres = st.selectbox("Genre",genres)

#             with col3:
#                 sort_by = st.selectbox("Sort",["Title (A-Z)", "Author (A-Z)", "Year(Newest)", "Added"])






# filtered_library = st.session_state.library.copy()
# if filter_status == "Read": # type: ignore
#     filtered_library = [b for b in filtered_library if b["read"]]

# elif filter_status == "Uread": # type: ignore
#     filtered_library =[b for b in filtered_libraryif not b["read"]]


# if filter_genre !="All": # type: ignore
#     filtered_library = [b for b in filtered_library if b["genre"] == filter_genre] # type: ignore


# if sort_by == "Title(A-Z)": # type: ignore
#     filtered_library.sort(key=lambda x:x["title"])

# elif sort_by == "Author(A-Z)": # type: ignore
#     filtered_library.sort(key=lambda x:x["author"])
    

# elif sort_by =="Year(Newest)": # type: ignore
#     filtered_library.sort(key=lambda x:x["year"],reverse=True)



# elif sort_by == "Added": # type: ignore
#     filtered_library.sort(key=lambda x:x["date_added"], reverse=True)



# if not filtered_library:
#     st.markdown(
#         """
#          <div class="empty-state">
#          <div class="empty-icon">📚</div>
#          <p>🕳Your Libray is Empty. Add Some Books to Begin !</p>
#          </div>
#        """,
#        unsafe_allow_html=True
#     )


# else:
#     st.markdown(f"<p style='color: #6b7280; margin-bottom: 1rem;'>{len(filtered_library)} books</p>",
#                 unsafe_allow_html=True
#                 )

# for book in filtered_library:
#     with st.container():
#         card_class = "book-card read-card" if book["read"] else "book-card unread-card"
#         st.markdown(f
#                     """
#                      <div class="{card_class}",
#                      <div>
#                      <div class="book-title">{book["title"]}</div>
#                      <div class="book-meta">by{book["author]} * {book["year"]} * {book["genre"]}</div>
#                      <div style="margin-top:0.75rem:">
#                            <span class="status-badge{"read-badge" if book["read] else "unread-badge"}">
#                            {"Read" if book['read'] else 'Unread'}
#                            </span>
#                            </div>
#                            </div>
#                            </div>



#                      """,
#                      unsafe_allow_html=True
#                      )
        


#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button(f"{"Mark Unred" if book['read'] else 'Mark Read'}",key=f"toggle_{book['id']}",type="primary"):
#                 toggle_read_status(book['id']) # type: ignore


#             st.rerun()
#         with col2:
#             if st.button("Remove", key=f"remove_{book["id"]}",type="secondary"):
#                 remove_book(book['id'])
#                 st.rerun()


#         with tabs[1]:
#             st.header("Add a New Book")
#             with st.container():
#                 col1,col2 = st.columns(2)
#                 with col1:
#                     title = st.text_input("Title", placeholder="Book Title")
#                     author = st.text_input("Author", placeholder="Author Name")
#                     year = st.text_input("Year", placeholder="e.g , @2025")

#                 with col2:
#                     genre = st.selectbox("Genre",["Fiction","Non-Fiction","Mystery","Sci-Fi","Fantasy",
#                          "Biography","History","Self-Help","Romance","Horror",
#                          "Thriller","Poetry","Science","Technology","Philosophy","Other"])
#                     read_status = st.radio("Read Status",["Read","Unread"],horizontal=True)

#                 if st.button("Add to Library", type="primary"):
#                     if add_book(title, author, year, genre, read_status="Read"):
#                         st.success(f"Added '{title}' successfully!")

#         with tabs[2]:
#             st.header("Search for a Book")
#             with st.container():
#                 col1,col2 = st.columns([3,1] gap="small")
#                 with col1:
#                     search_term = st.text_input("Search", placeholder="Enter Search term:...",label_visibility="collapsed")

#                 with col2:
#                     search_by = st.selectbox("Search by", ["title","author","year","genre"],label_visibility="collapsed")


                
#                 if search_term:
#                     results= search_books(search_term,search_by)
#                     if results:
#                         st.subheader(f"{len(results)} Results")
#                         for book in results:
#                             card_class = "book-card read-card" if book["read"] else "book-card unread-card"
#                             st.markdown(f"""
#                                  <div class="{card_class}">
#                                     <div>
#                                     <div class="book-title">{book['title']}</div>
#                                     <div class="book-meta">by {book['author']} * {book['year']} * {book['genre']}</div>
#                                     <div style="margin-top: 0.75rem">
#                                          <span class="status-badge {'read-badge' if book['read'] else 'unread-badge'}">
#                                             {'Read' if book['read'] else 'Unread'}
#                                     </span>
#                                     </div>
                                    
#                                     </div>
#                                  </div>
#                                        """,
#                                        unsafe_allow_html=True
#                                        )
                            

#                         else:
#                             st.info("No Matching books found:")

#                     else:
#                         st.info("Enter a Search term to Begin:")


#             with tabs[3]:
#                 st.subheader("Reading Insights")
#                 stats = get_statistics()
#                 col1,col2,col3 = st.columns(3)
#                 with col1:
#                     st.markdown(
#                         """
#                     <div class="stat-card">
#                        <div class= "stat-icon">📚</div>
#                        <div class="stat-value">{}</div>
#                        <div class="stat-title">Total Books</div>
#                        </div>
                  
#                              """.format(stats["total"]), unsafe_allow_html=True
#                     )

#                 with col2:
#                     st.markdown(
#                         """
#                          <div class="stat-card">
#                          <div class="stat-icon">✅ </div>
#                          <div class ="stat-title"> Book Read </div>
#                          </div>
#                      """.format(stats["read"]),unsafe_allow_html=True
#                     )
                
#                 with col3:
#                     st.markdown(
#                         """
#                         <div class="stat-card">
#                         <div class="stat-icon">🏐</div>
#                         <div class="stat-value">{:. if}% </div>
#                         <div class = stat-title"> Completion </div>
#                         </div>
#                           """
#                           .format(stats["percentage"]),unsafe_allow_html=True
#                     )





#     st.markdown(
#         """
#            <div class="footer">
#            <p>✡AZ Pesonal Library Manger </p>
#            <p> Made With 🚀 by 
#            <a href ="https://my-portfolio-3zxyofq3u-azeezullahs-projects.vercel.app"> ©Azeezullah Noohpoto </a>
#            </div>
#            """,
#            unsafe_allow_html=True
#     )






import streamlit as st
import json
import os
import random
from datetime import datetime

st.set_page_config(
    page_title="✡AZ Personal Library Manager",
    page_icon="📃",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS Style Fixes
st.markdown(
    """
    <style>
        .welcome-banner {
            background: linear-gradient(135deg, #6366f1, #4f46e5);
            color: white;
            padding: 2rem;
            border-top-right-radius: 12px;
            border-top-left-radius: 12px;
            text-align: center;
        }
        h1, h2, h3 {
            text-align: center;
            margin-bottom: 1rem;
        }
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            font-weight: 500;
            color: white;
            height: 2.75rem;
        }
        .primary-button {
            background: linear-gradient(135deg, #6b7280, #4b5563) !important;
        }
        .secondary-btn {
            background: linear-gradient(135deg, #f59e0b, #d97706) !important;
        }
        .danger-btn {
            background: linear-gradient(135deg, #ef4444, #dc2626) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def load_library():
    if os.path.exists("library.json"):
        try:
            with open("library.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            st.error("Error loading library file. Starting with an empty library.")
    return []

def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

def add_book(title, author, year, genre, read_status):
    if not title or not author:
        st.error("Title and Author are required.")
        return False
    
    try:
        year = int(year)
        if not (1000 <= year <= datetime.now().year):
            st.error(f"Year must be between 1000 and {datetime.now().year}.")
            return False
    except ValueError:
        st.error("Year must be a valid number.")
        return False
    
    book = {
        "id": str(random.randint(10000, 99999)),
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status == "Read",
        "date_added": datetime.now().strftime("%Y-%m-%d")
    }
    st.session_state.library.append(book)
    save_library(st.session_state.library)
    return True

def remove_book(book_id):
    st.session_state.library = [b for b in st.session_state.library if b["id"] != book_id]
    save_library(st.session_state.library)

def toggle_read_status(book_id):
    for book in st.session_state.library:
        if book["id"] == book_id:
            book["read"] = not book["read"]
            save_library(st.session_state.library)
            break

def get_statistics():
    total_books = len(st.session_state.library)
    read_books = sum(1 for book in st.session_state.library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    return {
        "total": total_books,
        "read": read_books,
        "unread": total_books - read_books,
        "percentage": percentage_read
    }

if "library" not in st.session_state:
    st.session_state.library = load_library()

# UI Rendering
st.markdown("""
    <div class="welcome-banner">
        <h1>✡AZ Personal Library Manager</h1>
    </div>
""", unsafe_allow_html=True)

tabs = st.tabs(["📚 Library", "+ Add Book", "🏸 Search", "🚠 Insights"])

# Library Tab
with tabs[0]:
    st.header("🚋 My Library")
    
    if not st.session_state.library:
        st.warning("Your library is empty. Add some books to get started!")
    else:
        for book in st.session_state.library:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']})")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"{'Mark Unread' if book['read'] else 'Mark Read'}", key=f"toggle_{book['id']}"):
                    toggle_read_status(book['id'])
                    st.rerun()
            with col2:
                if st.button("Remove", key=f"remove_{book['id']}"):
                    remove_book(book['id'])
                    st.rerun()

# Add Book Tab
with tabs[1]:
    st.header("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.text_input("Year")
    genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Mystery", "Sci-Fi", "Fantasy", "Other"])
    read_status = st.radio("Read Status", ["Read", "Unread"], horizontal=True)
    if st.button("Add to Library"):
        if add_book(title, author, year, genre, read_status):
            st.success(f"Added '{title}' successfully!")
            st.rerun()

# Insights Tab
with tabs[3]:
    st.subheader("Reading Insights")
    stats = get_statistics()
    st.write(f"**Total Books:** {stats['total']}")
    st.write(f"**Books Read:** {stats['read']}")
    st.write(f"**Completion Percentage:** {stats['percentage']:.2f}%")

st.markdown("""
    <div style="text-align:center; padding:20px; margin-top:30px; color:#9ca3af;">
        <p>✡AZ Personal Library Manager</p>
        <p>Made with 🚀 by <a href="https://my-portfolio-3zxyofq3u-azeezullahs-projects.vercel.app">©Azeezullah Noohpoto</a></p>
    </div>
""", unsafe_allow_html=True)

