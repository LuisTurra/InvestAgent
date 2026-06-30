def format_financial(value):
  
    try:
        if value is None:
            return "-"

        if isinstance(value, (int, float)):

           
            if value > 1000:
                return f"{value:,.2f}"

           
            if abs(value) < 0.01:
                return f"{value:.4f}"

          
            if 0 <= value <= 100:
                return f"{value:.1f}"

            return f"{value:.2f}"

        return str(value)

    except:
        return str(value)