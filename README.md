```markdown
# Aigeon AI: Real-Time Image Search

Aigeon AI's Real-Time Image Search is a Python-based server application designed to facilitate efficient and customizable image searches across the web. Leveraging the capabilities of the FastMCP framework, this application allows users to perform real-time image searches with a wide range of customizable filters, similar to those available in Google Images.

## Features Overview

- **Real-Time Image Search**: Perform searches for images across the web in real-time.
- **Customizable Search Filters**: Utilize a variety of search filters to refine image search results.
- **Integration with FastMCP**: Built on the FastMCP framework for efficient server operations.
- **Flexible Query Parameters**: Supports numerous parameters to tailor search results to specific needs.

## Main Features and Functionality

The application provides a robust set of features to enhance the image search experience:

- **Search Query**: Specify keywords to search for relevant images.
- **Result Limitation**: Control the number of search results returned, with a default of 10 and a maximum of 100.
- **Image Size Filtering**: Filter images based on size, from icons to large megapixel images.
- **Color Filtering**: Search for images with a dominant color, including options like red, blue, grayscale, and more.
- **Image Type Filtering**: Specify the type of images to search, such as photos, clipart, or animated images.
- **Time-Based Filtering**: Limit search results to images updated within a specific time range, such as the past day or year.
- **Usage Rights**: Filter images based on usage rights, including creative commons and commercial use.
- **File Type Filtering**: Search for images in specific file formats like JPG, PNG, GIF, etc.
- **Aspect Ratio Filtering**: Find images with specific aspect ratios, such as tall, square, or panoramic.
- **Country and Region Filtering**: Search for images published in specific countries or regions.
- **Safe Search Options**: Control the display of explicit content in search results with options like off, blur, or on.
- **Field Projection**: Customize the fields returned in the search response, such as title, size, and thumbnail URL.

## Main Functions Description

### `search_images`

The core function of the application, `search_images`, allows users to perform detailed and customized image searches. Below is a description of its parameters:

- **query**: A string representing the search query or keyword.
- **limit**: An integer or float indicating the maximum number of results to return. Defaults to 10.
- **size**: A string specifying the desired image size, with options ranging from 'any' to specific megapixel sizes.
- **color**: A string to filter images by dominant color, such as 'red', 'blue', or 'grayscale'.
- **type**: A string to filter images by type, such as 'photo' or 'animated'.
- **time**: A string to filter images by the time they were last updated, such as 'day' or 'year'.
- **usage_rights**: A string to filter images based on usage rights, like 'creative_commons'.
- **file_type**: A string to specify the desired image file format, such as 'jpg' or 'png'.
- **aspect_ratio**: A string to filter images by aspect ratio, such as 'tall' or 'panoramic'.
- **country**: A string representing the 2-letter country code for images published in a specific region.
- **safe_search**: A string to control the display of explicit content, with options like 'off' or 'blur'.
- **region**: A string representing the 2-letter country code for the region from which to make the query.
- **fields**: A string specifying a comma-separated list of image fields to include in the response.

This function returns a dictionary containing the search results, providing a comprehensive and customizable image search experience.

---

This README provides an overview of the Aigeon AI Real-Time Image Search application, highlighting its main features and functionality. The application is designed to offer a powerful and flexible tool for conducting image searches with precision and ease.
```