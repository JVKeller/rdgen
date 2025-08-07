"""
Custom middleware to handle development-specific header modifications
"""

class DevelopmentSecurityMiddleware:
    """
    Middleware to remove problematic security headers in development
    that cause browsers to enforce HTTPS
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Remove headers that cause HTTPS enforcement in development
        headers_to_remove = [
            'Cross-Origin-Opener-Policy',
            'Cross-Origin-Embedder-Policy',
            'Strict-Transport-Security',
            'Content-Security-Policy',
        ]
        
        for header in headers_to_remove:
            if header in response:
                del response[header]
        
        # Set permissive headers for development
        response['X-Frame-Options'] = 'SAMEORIGIN'
        response['X-Content-Type-Options'] = 'nosniff'
        
        return response
