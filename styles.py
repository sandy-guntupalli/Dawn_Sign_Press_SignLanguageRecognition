import math

def page_setup():
    return """
    <style>

         /* Hide side toolbar buttons*/
        div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }

        /* deccrease upper padding */
        .st-emotion-cache-gh2jqd {
            width: 100%;
            padding: 0rem 1rem 10rem;
            max-width: 46rem;
        }

        /* hide header */
        header {
        visibility: hidden;
        height: 0%;
        }


        .st-emotion-cache-1u2dcfn {
        display:none;
        }

        [data-testid="stSidebarNavSeparator"]{
        display: none;
        }
        [data-testid="stSidebarNavItems"] {
            max-height: none;
            font-family: 'Century Gothic', sans-serif;
        }

        /* Apply Century Gothic font to the entire app */
        * {
            font-family: 'Century Gothic', sans-serif;
        }

        /* Apply Century Gothic font to the whole app */
        * {
            font-family: 'Century Gothic', sans-serif;
        }
        
        /* Specific styling for the title */
        .st-bd h1 {
            font-family: 'Century Gothic', sans-serif;
        }

    </style>
    """
    
def page_with_webcam_video():
    return """
        <style>

        /* Image styling */
        img {
        border-radius: 1rem;
        height: 450px;
        width: 350px;
        }

        /* Image container styling */
        .image-container {
            position: relative;
            width: 100%;
            display: flex; /* Use flexbox */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            padding: 2rem;
        }

        /* Image wrapper styling */
        .image-wrapper {
        background-color: white;
        display: inline-block;
        width: 350px;
        height: 450px;
        overflow: hidden;
        position: relative;
        border-radius: 1rem; 
        align-content: center;
        }

        /* Text overlay on image */
        .text-overlay {
            position: absolute; 
            left: 6%;
            bottom: -7%;
            color: #683aff;
            font-size: 150px;
            z-index: 2;
            text-align: center; /* Center the text horizontally */
        }

        /* Quiz question text */
        .question-text {
        font-family: 'Century Gothic', sans-serif;
        font-size: 18px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 20px;
        }

        /* Button styling */
        .st-emotion-cache-11to1yi {
        width: 100%;
        }   

        .st-emotion-cache-1gv5c5a p {
            word-break: break-word;
            margin-bottom: 0px;
            font-size: 25px;
        }
    
        </style>
    """
