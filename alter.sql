

ALTER TABLE IF EXISTS public.article
ADD FOREIGN KEY (pubID) REFERENCES public.publications (pubID);

ALTER TABLE public.article
 ADD articleID SERIAL PRIMARY KEY;
 
 ALTER TABLE public.article
 ADD pubID int;
 
 ALTER TABLE public.proceedings 
 ADD CONSTRAINT fk_pubID FOREIGN KEY (pubID) REFERENCES public.publications (pubID) 
 ON DELETE CASCADE ON UPDATE CASCADE; 
 
 