# ProProofread Hub

A comprehensive AI-powered and human-verified text proofreading platform built with Streamlit.

## Features

### Free Tier
- ✅ **Community/Human Proofreading** - Submit text for peer review (5 free slots)
- ✅ **AI Proofreader** - Instant grammar and spelling corrections (5 free checks)
- ✅ **Multiple Languages** - Support for English, Spanish, French, German, Mandarin, and more
- ✅ **Regional Dialects** - American, British, Australian, Canadian, and Neutral options

### Premium Tier (Unlimited)
- 🚀 **Deep Stylistic Review** - Advanced linguistic analysis with professional tone calibration
- 🔍 **Plagiarism Detection** - Check text against millions of sources for originality
- 👨‍💼 **Expert Escalation** - Connect with dedicated professional editors
- 📊 **Advanced Analytics** - Track submissions, improvements, and usage statistics
- 🎯 **Tone Optimization** - Executive, Technical, Academic, and Creative copywriting modes
- 📁 **Export Options** - Download as PDF or DOCX

## Payment Integration

- **PayPal** - Secure payment processing with PayPal Smart Buttons
- **Stripe** - Credit card payments via Stripe Checkout

## Installation

1. Clone the repository:
```bash
git clone https://github.com/joaquimmurenga56-dev/ProProofread-Hub.git
cd ProProofread-Hub
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your actual API keys
```

5. Run the application:
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Configuration

### PayPal Setup
1. Go to [PayPal Developer Console](https://developer.paypal.com/)
2. Create a Sandbox or Live application
3. Copy your Client ID and Secret
4. Add to `.env`:
   ```
   PAYPAL_CLIENT_ID=your_client_id
   PAYPAL_SECRET=your_secret
   PAYPAL_MODE=sandbox  # or 'live'
   ```

### Stripe Setup
1. Go to [Stripe Dashboard](https://dashboard.stripe.com/)
2. Get your Secret and Public keys
3. Create Price IDs for products (Full Access $10, 24-Hour Pass $2)
4. Add to `.env`:
   ```
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_PUBLIC_KEY=pk_test_...
   STRIPE_PRICE_ID_FULL_ACCESS=price_...
   STRIPE_PRICE_ID_DAY_PASS=price_...
   ```

### Database Setup
1. For SQLite (default):
   ```
   DATABASE_URL=sqlite:///proproofread.db
   ```

2. For PostgreSQL:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/proproofread_db
   ```

## Project Structure

```
ProProofread-Hub/
├── app.py                 # Main application entry point
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── pages/
│   ├── free_tier.py      # Free tier UI components
│   └── premium_tier.py   # Premium tier UI components
├── utils/
│   ├── session_manager.py    # Session state management
│   ├── payment_handler.py    # PayPal & Stripe integration
│   ├── ai_service.py         # AI processing service
│   └── database.py           # Database models and operations
└── README.md             # This file
```

## Usage

### For Free Tier Users
1. Submit text for community review
2. Use AI proofreader with language/dialect selection
3. Upgrade to Premium when limits are reached

### For Premium Users
1. Access unlimited AI proofreading
2. Run deep stylistic analysis
3. Check plagiarism and originality
4. Request expert review
5. View analytics and history

## API Integrations (To Implement)

- **OpenAI GPT** - For AI proofreading and stylistic analysis
- **Turnitin or Copyscape** - For plagiarism detection
- **Expert Review System** - Backend queue for expert editors
- **Email Service** - For notifications and reports

## Development

To contribute:
1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Create a Pull Request

## Testing

Run tests with:
```bash
pytest tests/
```

## Deployment

### Streamlit Cloud
1. Push to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with GitHub integration

### Docker
```bash
docker build -t proproofread-hub .
docker run -p 8501:8501 proproofread-hub
```

## Troubleshooting

### Payment Not Processing
- Verify API keys are correct
- Check that URLs match your deployment domain
- Review payment provider logs

### Session State Issues
- Clear browser cache
- Restart Streamlit app
- Check browser console for errors

### Database Errors
- Ensure DATABASE_URL is correct
- Verify database credentials
- Check database connectivity

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- GitHub Issues: [ProProofread-Hub/issues](https://github.com/joaquimmurenga56-dev/ProProofread-Hub/issues)
- Email: support@proproofread.hub

## Roadmap

- [ ] Multi-language support for UI
- [ ] Mobile app (iOS/Android)
- [ ] Collaboration features for team editing
- [ ] API for third-party integrations
- [ ] Advanced ML models for tone detection
- [ ] Real-time collaborative editing
- [ ] Integration with Google Docs/Microsoft Word
- [ ] Voice input for proofreading
