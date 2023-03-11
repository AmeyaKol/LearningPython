mystr = 'Dune is a 2021 American epic science fiction film directed by Denis Villeneuve from a screenplay by Villeneuve, Jon Spaihts, and Eric Roth.'


class Span:
    def __init__(self, category, start, end):
        self.category = category
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.category}: [{self.start}, {self.end}]"
    # used to create a standard representation of the span, this will be returned if the print method is called
    def __eq__(self, other):
        if not isinstance(other, Span):
            return False
        return self.category == other.category and self.start == other.start and self.end == other.end
    #overloading the == operator, will check if two spans are equal
    def merge(self, other):
        if self.category != other.category:
            print("Cannot merge, different categories")
            return False
        if self.start <= other.start <= self.end + 1 or other.start <= self.start <= other.end + 1:
            self.start = min(self.start, other.start)
            self.end = max(self.end, other.end)
            return True
        return False
    
    def overlaps(self, other):
        return self.start <= other.end and self.end >= other.start
    # there is some intermediate overlapping range eg: S1(1,5) S2(4,7)

    def subsumes(self, other):
        return self.start <= other.start and self.end >= other.end
    # one span is compeletely contained within another span eg: S1(1,8) S2(2,5)

    @staticmethod
    def getspans(mystr):
        spacelist = [i for i in range(len(mystr)) if mystr[i]==' ']
        spacelist.insert(0,-1)
        retlist = [(spacelist[i]+1,spacelist[i+1]) for i in range(len(spacelist)-1)]
        return retlist
    
    @staticmethod
    def find_unlabeled_spans(text, spans):
        unlabeled_spans = []
        last_end = 0
        for span in sorted(spans, key=lambda x: x.start):
            if last_end < span.start:
                unlabeled_spans.append(Span("", last_end, span.start - 1))
            last_end = span.end + 1
        if last_end < len(text):
            unlabeled_spans.append(Span("", last_end, len(text) - 1))
        return unlabeled_spans

    @staticmethod
    def remove_overlap(span1, span2):
        if not span1.overlaps(span2):
            return span1, span2
        if span1.subsumes(span2):
            return span1, None
        if span2.subsumes(span1):
            return None, span2
        if span1.start < span2.start:
            return Span(span1.category, span1.start, span2.start - 1), Span(span2.category, span2.start, span2.end)
        else:
            return Span(span1.category, span2.end + 1, span1.end), Span(span2.category, span2.start, span2.end)

    @staticmethod
    def overlap_length(span1, span2):
        if not span1.overlaps(span2):
            return 0
        return min(span1.end, span2.end) - max(span1.start, span2.start) + 1

    @staticmethod
    def has_overlapping_spans(spans):
        sorted_spans = sorted(spans, key=lambda x: x.start)
        print(sorted_spans)
        for i in range(len(sorted_spans) - 1):
            if sorted_spans[i].overlaps(sorted_spans[i+1]):
                return True
        return False

myspans=[]

newspans = Span.find_unlabeled_spans(mystr,myspans)
print(newspans)
spanlist = [Span("",i[0],i[1]) for i in Span.getspans(mystr)]
print(spanlist)
print('\n\n')
val=Span.has_overlapping_spans(spanlist)
print(val)