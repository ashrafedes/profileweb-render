import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _neg2_utils import load_articles, save_articles, download_hero, make_neg_article, read_file

# Article metadata: (file, slug, category, tags, date_offset, reading_time, seo_title, meta_desc, keywords)
ARTICLES = [
    {
        'file': 'neg2_a01.txt',
        'slug': 'foundations-of-negotiation',
        'category': 'Negotiation',
        'tags': ['negotiation', 'batna', 'zopa', 'behavioral economics', 'principled negotiation'],
        'date_offset': 0,
        'reading_time': 20,
        'seo_title': 'Foundations of Negotiation: Theory & Practice',
        'meta_desc': 'Master negotiation fundamentals: distributive vs integrative, BATNA, ZOPA, anchoring, and behavioral economics in one comprehensive guide.',
        'keywords': ['negotiation foundations', 'distributive negotiation', 'integrative negotiation', 'BATNA', 'ZOPA', 'principled negotiation', 'behavioral economics', 'Harvard negotiation method'],
    },
    {
        'file': 'neg2_a02.txt',
        'slug': 'batna-mastery-negotiation',
        'category': 'Negotiation',
        'tags': ['batna', 'negotiation power', 'reservation price', 'walk away'],
        'date_offset': 1,
        'reading_time': 18,
        'seo_title': 'BATNA Mastery: Your Negotiation Power Source',
        'meta_desc': 'Develop and leverage your BATNA for negotiation power. Learn reservation price, ZOPA relationship, and advanced BATNA strategies.',
        'keywords': ['BATNA', 'best alternative to negotiated agreement', 'reservation price', 'negotiation power', 'walk away point', 'ZOPA', 'negotiation leverage'],
    },
    {
        'file': 'neg2_a03.txt',
        'slug': 'zopa-zone-of-possible-agreement',
        'category': 'Negotiation',
        'tags': ['zopa', 'negotiation', 'settlement zone', 'agreement'],
        'date_offset': 2,
        'reading_time': 18,
        'seo_title': 'ZOPA Explained: Zone of Possible Agreement',
        'meta_desc': 'Navigate the Zone of Possible Agreement in negotiation. Learn to identify, expand, and leverage ZOPA for better outcomes.',
        'keywords': ['ZOPA', 'zone of possible agreement', 'negotiation settlement', 'reservation price', 'negotiation range', 'BATNA', 'negotiation strategy'],
    },
    {
        'file': 'neg2_a04.txt',
        'slug': 'anchoring-strategies-negotiation',
        'category': 'Negotiation',
        'tags': ['anchoring', 'first offer', 'negotiation tactics', 'cognitive bias'],
        'date_offset': 3,
        'reading_time': 19,
        'seo_title': 'Anchoring Strategies: Set & Counter First Offer',
        'meta_desc': 'Master anchoring in negotiation: when to make the first offer, how to set effective anchors, and how to counter extreme anchors.',
        'keywords': ['anchoring bias', 'first offer negotiation', 'anchor effect', 'negotiation tactics', 'cognitive bias', 'MESO', 'counter-anchor', 'negotiation psychology'],
    },
    {
        'file': 'neg2_a05.txt',
        'slug': 'high-stakes-negotiation',
        'category': 'Negotiation',
        'tags': ['high stakes', 'pressure', 'complexity', 'executive negotiation'],
        'date_offset': 4,
        'reading_time': 20,
        'seo_title': 'High-Stakes Negotiation: Master Pressure',
        'meta_desc': 'Master high-stakes negotiation under pressure. Learn psychological preparation, team strategies, and managing external factors.',
        'keywords': ['high stakes negotiation', 'negotiation under pressure', 'executive negotiation', 'negotiation psychology', 'team negotiation', 'crisis negotiation', 'negotiation preparation'],
    },
    {
        'file': 'neg2_a06.txt',
        'slug': 'salary-negotiation-mastery',
        'category': 'Negotiation',
        'tags': ['salary', 'compensation', 'career', 'job offer'],
        'date_offset': 5,
        'reading_time': 18,
        'seo_title': 'Salary Negotiation: Master Your Worth',
        'meta_desc': 'Master salary negotiation: market value, anchoring, total compensation, and advanced techniques for career advancement.',
        'keywords': ['salary negotiation', 'compensation negotiation', 'job offer negotiation', 'market value', 'total compensation', 'career advancement', 'negotiation tactics'],
    },
    {
        'file': 'neg2_a07.txt',
        'slug': 'procurement-negotiation-value',
        'category': 'Negotiation',
        'tags': ['procurement', 'supplier', 'cost', 'sourcing'],
        'date_offset': 6,
        'reading_time': 20,
        'seo_title': 'Procurement Negotiation: Drive Value',
        'meta_desc': 'Master procurement negotiation: Kraljic Matrix, should-cost analysis, competitive tension, and BATNA development strategies.',
        'keywords': ['procurement negotiation', 'supplier negotiation', 'Kraljic Matrix', 'should-cost analysis', 'total cost of ownership', 'competitive tension', 'sourcing strategy'],
    },
    {
        'file': 'neg2_a08.txt',
        'slug': 'contract-negotiation-structuring',
        'category': 'Negotiation',
        'tags': ['contract', 'risk allocation', 'legal', 'governance'],
        'date_offset': 7,
        'reading_time': 20,
        'seo_title': 'Contract Negotiation: Structure & Risk',
        'meta_desc': 'Master contract negotiation: commercial terms, risk allocation, governance, and key provisions for value protection.',
        'keywords': ['contract negotiation', 'risk allocation', 'limitation of liability', 'warranty', 'indemnification', 'force majeure', 'dispute resolution', 'change control'],
    },
    {
        'file': 'neg2_a09.txt',
        'slug': 'vendor-negotiation-relationships',
        'category': 'Negotiation',
        'tags': ['vendor', 'SLA', 'supplier relationship', 'governance'],
        'date_offset': 8,
        'reading_time': 19,
        'seo_title': 'Vendor Negotiation: Strategic Relationships',
        'meta_desc': 'Master vendor negotiation: SLA design, performance metrics, vendor selection, and relationship governance frameworks.',
        'keywords': ['vendor negotiation', 'service level agreement', 'SLA negotiation', 'vendor selection', 'vendor governance', 'performance metrics', 'supplier relationship management'],
    },
    {
        'file': 'neg2_a10.txt',
        'slug': 'sales-negotiation-revenue',
        'category': 'Negotiation',
        'tags': ['sales', 'pricing', 'margin', 'value selling'],
        'date_offset': 9,
        'reading_time': 19,
        'seo_title': 'Sales Negotiation: Maximize Revenue',
        'meta_desc': 'Master sales negotiation: value anchoring, defending price, MESO strategies, and protecting margin against procurement.',
        'keywords': ['sales negotiation', 'price negotiation', 'value selling', 'margin protection', 'MESO', 'decoy pricing', 'procurement tactics', 'revenue optimization'],
    },
    {
        'file': 'neg2_a11.txt',
        'slug': 'conflict-resolution-negotiation',
        'category': 'Negotiation',
        'tags': ['conflict resolution', 'Thomas-Kilmann', 'difficult conversations', 'mediation'],
        'date_offset': 10,
        'reading_time': 18,
        'seo_title': 'Conflict Resolution: Frameworks & Tools',
        'meta_desc': 'Master conflict resolution: Thomas-Kilmann modes, difficult conversations framework, and de-escalation techniques.',
        'keywords': ['conflict resolution', 'Thomas-Kilmann', 'difficult conversations', 'workplace conflict', 'mediation', 'de-escalation', 'conflict management', 'negotiation'],
    },
    {
        'file': 'neg2_a12.txt',
        'slug': 'cross-cultural-negotiation',
        'category': 'Negotiation',
        'tags': ['cross-cultural', 'international', 'Hofstede', 'global business'],
        'date_offset': 11,
        'reading_time': 20,
        'seo_title': 'Cross-Cultural Negotiation: Global Guide',
        'meta_desc': 'Master cross-cultural negotiation: Hofstede dimensions, Culture Map, communication styles, and bicultural intermediaries.',
        'keywords': ['cross-cultural negotiation', 'Hofstede cultural dimensions', 'Culture Map', 'international negotiation', 'high-context communication', 'guanxi', 'cultural intelligence'],
    },
    {
        'file': 'neg2_a13.txt',
        'slug': 'emotional-intelligence-negotiation',
        'category': 'Negotiation',
        'tags': ['emotional intelligence', 'EQ', 'tactical empathy', 'Chris Voss'],
        'date_offset': 12,
        'reading_time': 19,
        'seo_title': 'Emotional Intelligence in Negotiation',
        'meta_desc': 'Master EQ in negotiation: self-awareness, tactical empathy, labeling, and reading body language for better outcomes.',
        'keywords': ['emotional intelligence negotiation', 'EQ negotiation', 'tactical empathy', 'labeling technique', 'body language', 'Chris Voss', 'amygdala hijack', 'negotiation psychology'],
    },
    {
        'file': 'neg2_a14.txt',
        'slug': 'psychological-tactics-negotiation',
        'category': 'Negotiation',
        'tags': ['psychology', 'cognitive bias', 'Cialdini', 'influence'],
        'date_offset': 13,
        'reading_time': 20,
        'seo_title': 'Psychological Tactics in Negotiation',
        'meta_desc': 'Master psychological tactics: cognitive biases, Cialdini principles, framing, anchoring, and defending against manipulation.',
        'keywords': ['psychological tactics negotiation', 'cognitive bias', 'Cialdini influence', 'loss aversion', 'anchoring bias', 'framing effect', 'reciprocity', 'negotiation psychology'],
    },
    {
        'file': 'neg2_a15.txt',
        'slug': 'negotiation-ethics',
        'category': 'Negotiation',
        'tags': ['ethics', 'integrity', 'deception', 'professional conduct'],
        'date_offset': 14,
        'reading_time': 18,
        'seo_title': 'Negotiation Ethics: Boundaries & Practice',
        'meta_desc': 'Master negotiation ethics: frameworks, boundaries between influence and manipulation, and responding to unethical tactics.',
        'keywords': ['negotiation ethics', 'ethical negotiation', 'deception in negotiation', 'professional integrity', 'influence vs manipulation', 'ethical decision making', 'negotiation conduct'],
    },
    {
        'file': 'neg2_a16.txt',
        'slug': 'multi-party-negotiation',
        'category': 'Negotiation',
        'tags': ['multi-party', 'coalition', 'facilitation', 'single-text'],
        'date_offset': 15,
        'reading_time': 19,
        'seo_title': 'Multi-Party Negotiation: Coalitions & Process',
        'meta_desc': 'Master multi-party negotiation: coalition formation, single-text technique, process design, and facilitation strategies.',
        'keywords': ['multi-party negotiation', 'coalition formation', 'single-text technique', 'negotiation facilitation', 'Nash equilibrium', 'blocking coalition', 'consensus building', 'negotiation process design'],
    },
    {
        'file': 'neg2_a17.txt',
        'slug': 'crisis-negotiation-business',
        'category': 'Negotiation',
        'tags': ['crisis', 'de-escalation', 'FBI', 'BCSM', 'Chris Voss'],
        'date_offset': 16,
        'reading_time': 19,
        'seo_title': 'Crisis Negotiation Principles for Business',
        'meta_desc': 'Apply FBI crisis negotiation principles to business: Behavioral Change Stairway Model, tactical empathy, and de-escalation.',
        'keywords': ['crisis negotiation', 'behavioral change stairway model', 'BCSM', 'de-escalation', 'tactical empathy', 'FBI negotiation', 'business crisis', 'Chris Voss'],
    },
    {
        'file': 'neg2_a18.txt',
        'slug': 'negotiating-as-project-manager',
        'category': 'Negotiation',
        'tags': ['project management', 'PMP', 'scope', 'stakeholder', 'matrix'],
        'date_offset': 17,
        'reading_time': 20,
        'seo_title': 'Negotiating as a Project Manager: Complete Guide',
        'meta_desc': 'Master negotiation for project managers: scope changes, resource negotiation, schedule, budget, and stakeholder management.',
        'keywords': ['project manager negotiation', 'scope negotiation', 'resource negotiation', 'stakeholder negotiation', 'matrix organization', 'change control', 'PMP negotiation', 'project management'],
    },
    {
        'file': 'neg2_a19.txt',
        'slug': 'virtual-remote-negotiation',
        'category': 'Negotiation',
        'tags': ['virtual', 'remote', 'video', 'email', 'digital'],
        'date_offset': 18,
        'reading_time': 19,
        'seo_title': 'Virtual & Remote Negotiation: Complete Guide',
        'meta_desc': 'Master virtual negotiation: video techniques, phone strategies, email best practices, and building trust remotely.',
        'keywords': ['virtual negotiation', 'remote negotiation', 'video negotiation', 'email negotiation', 'digital negotiation', 'virtual trust building', 'online negotiation tactics'],
    },
    {
        'file': 'neg2_a20.txt',
        'slug': 'expert-negotiation-playbook',
        'category': 'Negotiation',
        'tags': ['expert', 'playbook', 'framework', 'mastery', 'advanced'],
        'date_offset': 19,
        'reading_time': 22,
        'seo_title': 'Expert Negotiation Playbook: Master System',
        'meta_desc': 'The complete negotiation playbook: five-phase system, decision trees, tactical sequences, and expert habits for mastery.',
        'keywords': ['negotiation playbook', 'expert negotiation', 'negotiation system', 'negotiation framework', 'negotiation mastery', 'negotiation decision tree', 'negotiation tactics', 'advanced negotiation'],
    },
]

def extract_title(content):
    """Extract title from the first ## heading."""
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('## '):
            return line[3:].strip()
    return 'Untitled'

def extract_excerpt(content):
    """Extract excerpt from the first paragraph after the title."""
    lines = content.split('\n')
    found_title = False
    for line in lines:
        line = line.strip()
        if line.startswith('## '):
            found_title = True
            continue
        if found_title and line and not line.startswith('#') and not line.startswith('---'):
            return line[:155]
    return ''

def main():
    articles = load_articles()
    existing_slugs = {a.get('slug', '') for a in articles}
    
    added = 0
    for i, meta in enumerate(ARTICLES):
        slug = meta['slug']
        if slug in existing_slugs:
            print(f'  SKIP: {slug} already exists')
            continue
        
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), meta['file'])
        content = read_file(filepath)
        
        title = extract_title(content)
        excerpt = extract_excerpt(content)
        
        # Use SEO title if provided, otherwise use extracted title
        seo_title = meta.get('seo_title', title)
        meta_desc = meta.get('meta_desc', excerpt)
        
        en = {
            'title': title,
            'excerpt': excerpt,
            'content': content,
            'metaTitle': seo_title + ' - Ashraf El Desoky, PMP',
            'metaDescription': meta_desc,
            'keywords': meta.get('keywords', []),
        }
        
        hero = download_hero(i, slug)
        
        article = make_neg_article(
            aid=f'neg2-{i+1:02d}',
            slug=slug,
            category=meta['category'],
            tags=meta['tags'],
            en=en,
            hero=hero,
            date_offset=meta.get('date_offset', i),
            reading_time=meta.get('reading_time', 18),
        )
        
        articles.append(article)
        added += 1
        print(f'  ADDED: {slug} ({title[:50]}...)')
    
    save_articles(articles)
    print(f'\nDone! Added {added} articles. Total articles: {len(articles)}')

if __name__ == '__main__':
    main()
